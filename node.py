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

    def broadcast_blockchain(self):
        # length = len(self.blockchain.blockchain_to_string().encode())
        self.client.sendto(self.blockchain.blockchain_to_string().encode(), (ip, port))
    
    def receive_blockchain(self):
        self.client.bind(("", port))
        data, addr = self.client.recvfrom(50000)
        print("received message: %s" % data.decode())
        return Blockchain.string_to_blockchain(data.decode())
    
    
    