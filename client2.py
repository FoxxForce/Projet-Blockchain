#!/usr/bin/env python3
from node import * 

if __name__ == "__main__":
    b = Block(None, "Hello")
    chain = Blockchain("client2")
    node = Node("225.1.2.5")
    node.blockchain = node.request_blockchain()
    node.run_node()