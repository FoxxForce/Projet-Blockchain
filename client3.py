#!/usr/bin/env python3
from node import * 
import threading

def thread_mining(wallet):
        new_block = Block(node.blockchain.chain[-1].hash(), wallet.get_public_key())
        new_block.proof_of_work()
        node.blockchain.add_block(new_block)
        node.broadcast_blockchain()

if __name__ == "__main__":
    wallet2 = Wallet()
    node = Node("225.1.2.5")
    node.request_blockchain()
    t = threading.Thread(target=thread_mining, args=(wallet2,))
    t.start()
    node.run_node()