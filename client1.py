#!/usr/bin/env python3
from node import * 


if __name__ == "__main__":  
    b = Block(None, "Hello")
    chain = Blockchain("okok")
    # b.proof_of_work()
    # print(b.hash())
    chain.add_block(b)
    # print(chain.is_valid_blockchain())
    print(chain.blockchain_to_string())
    node = Node(chain)
    node.broadcast_blockchain()
    #chain2 = node.receive_blockchain()
