#!/usr/bin/python`
__author__ = 'kilroy'
#  (c) 2014, WasHere Consulting, Inc.
#  Written for Infinite Skills

"""
 Fuzzying demo
 
 Fuzzying is sending some garbage data to a target.
 It is done to see if the target responds in unexpected way, 
 perhaps to go into debugging mode with root access.
 
"""
from pyfuzz.generator import *
import socket

msg = random_ascii() + b" / HTTP/1.1\nHost: 172.30.42.114\r\n"
print(msg)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("172.30.42.114", 80)
    s.connect(addr)
    s.sendall(msg)
    resp = s.recv(4096)
    print(resp)
except Exception as e:
    print(e)
finally:
    s.close()
