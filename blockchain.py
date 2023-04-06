#!/usr/bin/env python3

import hashlib
import json
import rsa

class Block():
    def __init__(self, previous_hash, data, wallet):
        self.previous_hash = previous_hash
        self.data = data
        self.difficulty = 5
        self.nonce = 0
        self.wallet = wallet
    
    # return the string representation of the block
    def string_block(self):
        return json.dumps(self.__dict__, sort_keys=True)
    
    # return the hash of the block
    def hash(self):
        return hashlib.sha256(self.string_block().encode()).hexdigest()
    
    # search a valid nonce for the block
    def proof_of_work(self):
        self.nonce = 0
        while not self.hash().startswith('0' * self.difficulty):
            self.nonce += 1
        return self.nonce

    def is_valid_block(self):
        for transaction in self.data:
            signature = bytes.fromhex(transaction["signature"])
            sender_public_key = rsa.PublicKey.load_pkcs1(transaction["sender"].encode())
            message = json.dumps(transaction, sort_keys=True)
            try:
                rsa.verify(message.encode(), signature, sender_public_key)
            except rsa.pkcs1.VerificationError:
                return False
        return self.hash().startswith('0' * self.difficulty)

    def add_transaction(self, sender, receiver, amount):
        transaction = {"sender": sender, "receiver": receiver, "amount": amount}
        signature = self.wallet.sign(json.dumps(transaction))
        transaction["signature"] = signature.hex()
        self.data.append(transaction)
    

class Blockchain():
    reward = 100

    def __init__(self, data=""):
        self.chain = [Block(None, data)]
        self.wallet = Wallet()
        self.current_block = Block(None, [], self.wallet)
        self.add_transaction(None, self.wallet.get_public_key(), self.reward)
    
    def length_blockchain(self):
        return len(self.chain)
    
    # verify the integrity of the blockchain
    def is_valid_blockchain(self):
        for i in range(1, len(self.chain)):
            if self.chain[i].previous_hash != self.chain[i-1].hash() and not self.chain[i].is_valid_block():
                return False
        return True
    
    # add a block to the blockchain
    def add_block(self, block):
        block.previous_hash = self.last_block().hash()
        block.proof_of_work()
        self.chain.append(block)
        self.current_block = Block(None, [], self.wallet)
        self.add_transaction(None, self.wallet.get_public_key(), self.reward)
        self.add_transaction(None, block.wallet.get_public_key(), self.reward)  # Ajout de la récompense pour le mineur
        return True

    
    def blockchain_to_string(self):
        l = []
        for block in self.chain:
            l.append(block.__dict__)
        return json.dumps(l)
    
    def string_to_blockchain(string):
        l = json.loads(string)
        chain = Blockchain()
        for block in l:
            chain.add_block(Block(block["previous_hash"], block["data"]))
        return chain

    def generate_keys(self):
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()
        return private_key, public_key

    def add_transaction(self, sender, receiver, amount):
        transaction = {"sender": sender, "receiver": receiver, "amount": amount}
        signature = self.wallet.sign(json.dumps(transaction))
        transaction["signature"] = signature.hex()
        self.current_block.data.append(transaction)
    
    def get_balance(self, address):
        balance = 0
        for block in self.chain:
            for transaction in block.data:
                if transaction["receiver"] == address:
                    balance += transaction["amount"]
                if transaction["sender"] == address:
                    balance -= transaction["amount"]
        return balance

class Wallet():
    def __init__(self):
        (self.public_key, self.private_key) = rsa.newkeys(512)
    
    def get_public_key(self):
        return self.public_key.save_pkcs1().decode()

    def sign(self, message):
        return rsa.sign(message.encode(), self.private_key, 'SHA-256')
    
"""t1 = "Cheikou envoie 2StoopidCoins a Hicham"
t2 = "Hicham envoie 1StoopidCoins a Cheikou"

block1 = Block(None, t1)
block2 = Block(block1.hash(), t2)

print(block1.data, "\n", block1.hash())
print("\n \n", block2.data, "\n", block2.hash())"""