#!/usr/bin/env python3
from node import * 

if __name__ == "__main__": 
    chain = Blockchain()
    node = Node("225.1.2.4")
    node.blockchain = chain
    node.run_node()

