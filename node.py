#!/usr/bin/env python3
from blockchain import *
import socket

port = 3023
ip = "255.255.255.255"
# Node Blockchain
# udp broadcast

class Node():
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # broadcast the blockchain to the network
    def broadcast_blockchain(self):
        self.client.sendto(self.blockchain.blockchain_to_string().encode(), (ip, port))
    
    # receive the blockchain from the network
    def receive_blockchain(self):
        self.client.bind(("", port))
        data, addr = self.client.recvfrom(50000)
        print("received message: %s" % data.decode())
        return Blockchain.string_to_blockchain(data.decode())
    
    # update the blockchain if the new blockchain is valid and longer than the current blockchain
    def update_blockchain(self, new_blockchain):
        if new_blockchain.length_blockchain() > self.blockchain.length_blockchain() and new_blockchain.is_valid_blockchain():
            self.blockchain = new_blockchain
    
    
    