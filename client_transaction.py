#!/usr/bin/env python3
from node import * 
import threading

if __name__ == "__main__":
    wallet_sender = Wallet()
    public_key_receiver = "-----BEGIN RSA PUBLIC KEY-----\nMEgCQQDEIsEdTe+hgpNszqsT8+xyOqMRAIQxeSyTh1HV0eKm0L+PPz0NJH6qBgG9\nRI6UF4wpO4mtutwySruFaFvns8HVAgMBAAE=\n-----END RSA PUBLIC KEY-----\n"
    amount = int(input("Enter the amount of the transaction: "))
    Node.send_transaction("225.1.2.5", wallet_sender, public_key_receiver, amount)