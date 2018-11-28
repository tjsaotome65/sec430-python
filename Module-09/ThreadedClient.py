#!/usr/bin/python
__author__ = 'kilroy'
#  (c) 2014, WasHere Consulting, Inc.
#  Written for Infinite Skills
#
# Modified and enhanced for RWU SEC 430
#
# T. J. Saotome

import socket
import threading

class clientConnect(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        addr = ("www.rwu.com", 443)
        sock.connect(addr)
        print(str(sock), "Connected")


sockClients = []
for i in range(1,100):
    s = clientConnect()
    s.start()
    print("started ", i)
    sockClients.append(s)
