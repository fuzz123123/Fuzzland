# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 19:55:56 2021

@author: Weiq
"""
from socket import *
import os, sys

ADDR = ('0.0.0.0', 8889)

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.blind(ADDR)
s.listen(5)

print(f'listening port {ADDR[-1]}')
while True:
    c, addr = s.accept()
    print('connected from addr', addr)
    
    pid = os.fork()
    if pid == 0:
        handle(c)
    else:
        # waiting for next client connection
        c.close()
