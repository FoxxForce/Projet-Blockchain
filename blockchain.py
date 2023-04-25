#!/usr/bin/env python3

import hashlib
import json
import rsa

class Transaction:
    def __init__(self, prodution_place, production_date, product_name, batch_id, sender_public_key, current_location, transported_to, date, signature=None):
        self.prodution_place = prodution_place
        self.production_date = production_date
        self.product_name = product_name
        self.batch_id = batch_id 
        self.current_location = current_location
        self.date = date
        self.transported_to = transported_to 
        self.sender_public_key = sender_public_key
        self.signature = signature


    def to_dict(self):
        return {
            "prodution_place": self.prodution_place,
            "production_date": self.production_date,
            "product_name": self.product_name,
            "batch_id": self.batch_id,
            "current_location": self.current_location,
            "date": self.date,
            "transported_to": self.transported_to,
            "sender_public_key": self.sender_public_key,
            "signature": self.signature
        }

   
    def message(self):
        return json.dumps({
            "prodution_place": self.prodution_place,
            "production_date": self.production_date,
            "product_name": self.product_name,
            "batch_id": self.batch_id,
            "current_location": self.current_location,
            "date": self.date,
            "transported_to": self.transported_to,
            "sender_public_key": self.sender_public_key
        }, sort_keys=True)
    
    def dict_to_transaction(d):
        return Transaction(prodution_place=d["prodution_place"], production_date=d["production_date"], product_name=d["product_name"], batch_id=d["batch_id"], 
                         current_location=d["current_location"], date=d["date"], transported_to=d["transported_to"],sender_public_key=d["sender_public_key"], signature=d["signature"])

    def sign_transaction(self, private_key):
        self.signature = rsa.sign(self.message().encode(), private_key, 'SHA-256').hex()
        
    def is_valid_transaction(self):
        signature = bytes.fromhex(self.signature)
        print(self.sender_public_key)
        sender_public_key = rsa.PublicKey.load_pkcs1(self.sender_public_key.encode())
        message = self.message()
        try:
            rsa.verify(message.encode(), signature, sender_public_key)
            return True
        except rsa.pkcs1.VerificationError:
            return False


    
class Block:
    def __init__(self, previous_hash, data=[]):
        self.previous_hash = previous_hash
        self.data = data
        self.difficulty = 1
        self.nonce = 0
    
    # return the string representation of the block
    def string_block(self):
        return json.dumps({
            "previous_hash": self.previous_hash,
            "data": [transaction.to_dict() for transaction in self.data],
            "difficulty": self.difficulty,
            "nonce": self.nonce
        }, sort_keys=True)
    
    # return the hash of the block
    def hash(self):
        return hashlib.sha256(self.string_block().encode()).hexdigest()
    
    # search a valid nonce for the block
    def proof_of_work(self):
        while not self.hash().startswith('0' * self.difficulty):
            self.nonce += 1
        return self.nonce

    def is_valid_block(self):
        return self.hash().startswith('0' * self.difficulty)

    def add_transaction(self, transaction):
        self.data.append(transaction)
    

class Blockchain():

    def __init__(self, data=[]):
        self.chain = [Block(None, data)]
        self.chain[0].proof_of_work() 
    
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
        self.chain.append(block)
        if not self.is_valid_blockchain() :
            self.chain.pop()
            return False
        return True

    def blockchain_to_string(self):
        l = []
        for block in self.chain:
            l.append(block.string_block())
        return json.dumps(l)
    
    
    def string_to_blockchain(string):
        l = json.loads(string)
        blockchain = Blockchain()
        for block in l:
            b = json.loads(block)
            blockchain.add_block(Block(b["previous_hash"], []))
            blockchain.chain[-1].difficulty = b["difficulty"]
            blockchain.chain[-1].nonce = b["nonce"]
            for transaction in b["data"]:
                blockchain.chain[-1].data.append(Transaction.dict_to_transaction(transaction))
        return blockchain
    
    def trace_drug(self, serial_number):
        l = []
        for block in self.chain:
            for transaction in block.data:
                if transaction.serial_number == serial_number:
                    l.append(transaction)
        l.sort(key=lambda x: x.date)
        return l
    
if __name__ == "__main__":
    blockchain = Blockchain()
    (public_key, private_key) = rsa.newkeys(512)
    #c'est une supply chain médicament 
    transaction = Transaction(1,  rsa.PublicKey.load_pkcs1(public_key), "pharmacie", "hopital", "10/10/2020")
    transaction.sign_transaction(private_key)
    block = Block(blockchain.chain[-1].hash(), [transaction])
    block.proof_of_work()
    blockchain.add_block(block)
    print(blockchain.blockchain_to_string())
