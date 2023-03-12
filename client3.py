#!/usr/bin/env python3
from node import * 
import threading

def thread_mining():
        new_block = Block(node.blockchain.chain[-1].hash(), "New Block")
        new_block.proof_of_work()
        node.blockchain.add_block(new_block)
        node.broadcast_blockchain()

if __name__ == "__main__":
    b = Block(None, "New Block")
    chain = Blockchain("client3")
    node = Node("225.1.2.5")
    node.blockchain = node.request_blockchain()
    t = threading.Thread(target=thread_mining)
    t.start()
    node.run_node()