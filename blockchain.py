#!/usr/bin/env python3

import hashlib
import json

class Block():
    def __init__(self, previous_hash, data):
        self.previous_hash = previous_hash
        self.data = data
        self.difficulty = 5
        self.nonce = 0
    
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
        return self.hash().startswith('0' * self.difficulty)
    
        
class Blockchain():
    def __init__(self, data=""):
        self.chain = [Block(None, data)]
    
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
            l.append(block.__dict__)
        return json.dumps(l)
    
    def string_to_blockchain(string):
        l = json.loads(string)
        chain = Blockchain()
        for block in l:
            chain.add_block(Block(block["previous_hash"], block["data"]))
        return chain

    


# b = Block(None, "Hello")
# chain = Blockchain("okok")
# b.proof_of_work()
# print(b.hash())
# chain.add_block(b)
# print(chain.is_valid_blockchain())