#!/usr/bin/env python3
from node import * 
import threading

if __name__ == "__main__":
    #crée un neoud de validation
    wallet_val = Wallet()
    node = Node_validation("225.1.2.4", wallet_val.get_public_key(), 2)
    node.run_node()