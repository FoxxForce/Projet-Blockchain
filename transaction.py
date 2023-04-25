#!/usr/bin/env python3
from node import * 
import threading


if __name__ == "__main__":
    (public_key, private_key) = rsa.newkeys(512)
    transaction_1 = Transaction(prodution_place='usine1', production_date='01/01/2023', 
                            product_name='medicament1', batch_id='1', 
                            sender_public_key=rsa.PublicKey.load_pkcs1(public_key), 
                            current_location='pharmacie1', transported_to='pharmacie2',
                            date='2022-01-02')
    transaction_1.sign_transaction(private_key)
    Node.send_transaction(transaction_1)