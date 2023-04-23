#!/usr/bin/env python3
from blockchain import *
import socket
import threading

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
        self.client.sendto(("SNDBL" + self.blockchain.blockchain_to_string()).encode(), (ip_broadcast, self.port))
    
    # receive the blockchain from the network
    def receive_blockchain(self):
        data, addr = self.client.recvfrom(50000)
        while not data.decode().startswith("SNDBL"):
            data, addr = self.client.recvfrom(50000)
        blockchain_string = data.decode()[5:]
        blockchain = Blockchain.string_to_blockchain(blockchain_string)
        if blockchain.is_valid_blockchain():
            self.blockchain = blockchain
        return blockchain

    def send_blockchain(self, addr):
        self.client.sendto(("SNDBL" + self.blockchain.blockchain_to_string()).encode(), addr)


    def run_node(self):
        print("Node running on port %d" % self.port)
        print(self.blockchain.blockchain_to_string())
        while True:
            data, addr = self.client.recvfrom(50000)
            print("received message: %s from %s" % (data.decode(), addr))
            if data.decode() == "REQBL":
                self.send_blockchain(addr)
            elif data.decode().startswith("SNDBL"):
                self.update_blockchain(Blockchain.string_to_blockchain(data.decode()[5:]))

    def send_transaction(ip, sender_wallet, receiver, amount):
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        client.sendto(("TRNSC" + json.dumps(sender_wallet.create_transaction(receiver, amount))).encode(), (ip_broadcast, port))
        client.close()
        
    
    # update the blockchain if the new blockchain is valid and longer than the current blockchain
    def update_blockchain(self, new_blockchain):
        if new_blockchain.length_blockchain() > self.blockchain.length_blockchain() and new_blockchain.is_valid_blockchain():
            self.blockchain = new_blockchain
            print("Blockchain updated")

class Node_validation(Node):
    def __init__(self, ip, public_key, nb_transactions):
        self.nb_transactions = nb_transactions
        self.public_key = public_key
        super().__init__(ip)
        self.request_blockchain()
        self.mining = False
        self.block = Block(self.blockchain.chain[-1].hash(), self.public_key)
        self.lock = threading.Lock()
    
    def thread_mining(self):
        print("mining block validation")
        self.block.proof_of_work()
        self.blockchain.add_block(self.block)
        self.broadcast_blockchain()
        self.block = Block(self.blockchain.chain[-1].hash(), self.public_key, [])

    def run_node(self):
        print("Node running on port %d" % self.port)
        print(self.blockchain.blockchain_to_string())
        while True:
            if len(self.block.data) >= self.nb_transactions and not self.mining:
                self.mining = True
                t = threading.Thread(target=self.thread_mining)
                self.lock.acquire()
                t.start()
                self.lock.release()
                self.mining = False
            data, addr = self.client.recvfrom(50000)
            print("received message: %s from %s" % (data.decode(), addr))
            if data.decode() == "REQBL":
                self.send_blockchain(addr)
            elif data.decode().startswith("SNDBL"):
                self.update_blockchain(Blockchain.string_to_blockchain(data.decode()[5:]))
            elif data.decode().startswith("TRNSC"):
                transaction = json.loads(data.decode()[5:])
                if self.blockchain.is_valid_transaction(transaction) and self.lock.acquire(False):
                    self.block.data.append(transaction)
                    print("Transaction added to block")
                    self.lock.release()
                else:
                    print("Invalid transaction")
                
    