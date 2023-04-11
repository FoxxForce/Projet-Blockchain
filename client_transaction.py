#!/usr/bin/env python3
from node import * 
import threading

if __name__ == "__main__":
    wallet_sender = Wallet()
    public_key_receiver = input("Enter the public key of the receiver: ")
    amount = int(input("Enter the amount of the transaction: "))
    Node.send_transaction("225.1.2.5", wallet_sender, public_key_receiver, amount)