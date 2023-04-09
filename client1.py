#!/usr/bin/env python3
from node import * 


if __name__ == "__main__": 
    wallet1 = Wallet() 
    b = Block(None, [], wallet1)
    chain = Blockchain(wallet1)
    chain.add_block(b)
    node = Node("225.1.2.4")
    node.blockchain = chain
    node.run_node()

