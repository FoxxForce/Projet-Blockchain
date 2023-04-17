#!/usr/bin/env python3

import hashlib
import json
import rsa

class Block():
    def __init__(self, previous_hash, miner_public_key, data=[]):
        self.previous_hash = previous_hash
        self.data = data
        self.difficulty = 5
        self.nonce = 0
        self.miner_public_key = miner_public_key
    
    # return the string representation of the block
    def string_block(self):
        return json.dumps(self.__dict__, sort_keys=True)
    
    # return the hash of the block
    def hash(self):
        return hashlib.sha256(self.string_block().encode()).hexdigest()
    
    # search a valid nonce for the block
    def proof_of_work(self):
        while not self.hash().startswith('0' * self.difficulty):
            self.nonce += 1
        return self.nonce

    def is_valid_block(self):
        for transaction in self.data:
            if not Wallet.is_valid_transaction(transaction):
                return False
        return self.hash().startswith('0' * self.difficulty)

    def add_transaction(self, sender_wallet, receiver, amount):
        transaction = {"sender": sender_wallet.get_public_key(), "receiver": receiver, "amount": amount}
        signature = sender_wallet.sign(json.dumps(transaction))
        transaction["signature"] = signature.hex()
        self.data.append(transaction)
    
    

class Blockchain():

    def __init__(self, creator_public_key, data=[]):
        self.reward = 100
        self.chain = [Block(None, creator_public_key, data)]
        self.chain[0].nonce = 547640
        self.chain[0].proof_of_work() 
    
    def length_blockchain(self):
        return len(self.chain)
    
    def is_valid_transaction(self, transaction):
        return Wallet.is_valid_transaction(transaction) and transaction["amount"] <= self.get_balance(transaction["sender"])
    
    # verify the integrity of the blockchain
    def is_valid_blockchain(self):
        for i in range(1, len(self.chain)):
            if self.chain[i].previous_hash != self.chain[i-1].hash() and not self.chain[i].is_valid_block():
                return False
            blockchain_tmp = Blockchain(self.chain[0].miner_public_key)
            blockchain_tmp.chain = self.chain[:i]
            for transaction in self.chain[i].data:
                if not blockchain_tmp.is_valid_transaction(transaction):
                    return False
        return True
    
    

    # add a block to the blockchain
    def add_block(self, block):
        self.chain.append(block)
        if not self.is_valid_blockchain() :
            self.chain.pop()
            return False
        return True

    
    def blockchain_to_string(self):
        l = []
        for block in self.chain:
            l.append(block.__dict__)
        return json.dumps(l)
    
    def string_to_blockchain(string):
        l = json.loads(string)
        blockchain = Blockchain(l[0]["miner_public_key"])
        blockchain.chain = []
        for block in l:
            blockchain.add_block(Block(block["previous_hash"],  block["miner_public_key"], block["data"]))
            blockchain.chain[-1].nonce = block["nonce"]
        return blockchain

    def generate_keys(self):
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()
        return private_key, public_key
    
    def get_balance(self, public_key):
        balance = 100
        for block in self.chain:
            for transaction in block.data:
                if transaction["receiver"] == public_key:
                    balance += transaction["amount"]
                if transaction["sender"] == public_key:
                    balance -= transaction["amount"]
            if block.miner_public_key == public_key:
                balance += self.reward
        return balance

class Wallet():
    def __init__(self):
        (self.public_key, self.private_key) = rsa.newkeys(512)
    def get_public_key(self):
        return self.public_key.save_pkcs1().decode()

    def sign(self, message):
        return rsa.sign(message.encode(), self.private_key, 'SHA-256')
    
    def is_valid_transaction(transaction):
        signature = bytes.fromhex(transaction["signature"])
        sender_public_key = rsa.PublicKey.load_pkcs1(transaction["sender"].encode())
        sign_temp = transaction.pop("signature", "")
        message = json.dumps(transaction, sort_keys=True)
        try:
            rsa.verify(message.encode(), signature, sender_public_key)
            transaction["signature"] = sign_temp
            return True
        except rsa.pkcs1.VerificationError:
            transaction["signature"] = sign_temp
            return False
    
    def create_transaction(self, receiver, amount):
        transaction = {"sender": self.get_public_key(), "receiver": receiver, "amount": amount}
        signature = self.sign(json.dumps(transaction, sort_keys=True))
        transaction["signature"] = signature.hex()
        return transaction
    
"""t1 = "Cheikou envoie 2StoopidCoins a Hicham"
t2 = "Hicham envoie 1StoopidCoins a Cheikou"

block1 = Block(None, t1)
block2 = Block(block1.hash(), t2)

print(block1.data, "\n", block1.hash())
print("\n \n", block2.data, "\n", block2.hash())"""