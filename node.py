#!/usr/bin/env python3
from blockchain import *
import socket

port = 3023
ip_broadcast = "255.255.255.255"
class Node():
    def __init__(self, ip):
        self.ip = ip
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.client.bind(("", self.port))
        self.blockchain = None

    # request the blockchain from the network
    def request_blockchain(self):
        self.client.sendto("REQBL".encode(), (ip_broadcast, self.port))
        self.receive_blockchain()
    # broadcast the blockchain to the network
    def broadcast_blockchain(self):
        self.client.sendto(self.blockchain.blockchain_to_string().encode(), (ip_broadcast, self.port))
    
    # receive the blockchain from the network
    def receive_blockchain(self):
        data, addr = self.client.recvfrom(50000)
        if data.decode() == "REQBL":
            data, addr = self.client.recvfrom(50000)
        blockchain_string = data.decode()
        blockchain = Blockchain.string_to_blockchain(blockchain_string)
        if blockchain.is_valid_blockchain():
            self.blockchain = blockchain
        return blockchain

    def send_blockchain(self, addr):
        self.client.sendto(self.blockchain.blockchain_to_string().encode(), addr)


    def run_node(self):
        print("Node running on port %d" % self.port)
        print(self.blockchain.blockchain_to_string())
        while True:
            data, addr = self.client.recvfrom(50000)
            print("received message: %s from %s" % (data.decode(), addr))
            if data.decode() == "REQBL":
                self.send_blockchain(addr)
            else:
                self.update_blockchain(Blockchain.string_to_blockchain(data.decode()))
           
    
    # update the blockchain if the new blockchain is valid and longer than the current blockchain
    def update_blockchain(self, new_blockchain):
        if new_blockchain.length_blockchain() > self.blockchain.length_blockchain() and new_blockchain.is_valid_blockchain():
            self.blockchain = new_blockchain
            print("Blockchain updated")
            print(self.blockchain.blockchain_to_string())

    
    
    