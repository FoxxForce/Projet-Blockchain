#!/usr/bin/env python3
from node import * 

if __name__ == "__main__":
    wallet2 = Wallet()
    b = Block(None, "Hello", wallet2.get_public_key())
    chain = Blockchain("client2")
    node = Node("225.1.2.5")
    node.request_blockchain()
    node.run_node()