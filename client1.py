#!/usr/bin/env python3
from node import * 

if __name__ == "__main__": 
    chain = Blockchain("-----BEGIN RSA PUBLIC KEY-----\nMEgCQQCNWrAHU+j4fs2TL/V7tY/ng/urX92Op8rP0XtD7QqQ+UGdi7pzsLjNsPv3\nzuVpoaXNQshH3QEXgBuLQjlyvMWlAgMBAAE=\n-----END RSA PUBLIC KEY-----\n")
    node = Node("225.1.2.4")
    node.blockchain = chain
    node.run_node()

