#!/usr/bin/env python3
from node import * 
import threading

def thread_mining(transaction=[]):
        new_block = Block(node.blockchain.chain[-1].hash())
        new_block.proof_of_work()
        node.blockchain.add_block(new_block)
        node.broadcast_blockchain()

if __name__ == "__main__":
    node = Node("225.1.2.5")
    node.request_blockchain()
    t = threading.Thread(target=thread_mining, args=())
    t.start()
    node.run_node()