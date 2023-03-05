#!/usr/bin/env python3
from node import * 

if __name__ == "__main__":
    b = Block(None, "Hello")
    chain = Blockchain("client2")
    node = Node(chain)
    chain2 = node.receive_blockchain()
    print(chain2.blockchain_to_string())