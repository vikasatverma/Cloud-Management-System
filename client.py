#!/usr/bin/python3           # This is client.py file

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = "192.168.122.58"                           

port = 9999

# connection to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes
msg = s.recv(1024)                                     


print (msg.decode('ascii'))

msg = "a car!" + "\r\n"

s.send(msg.encode('ascii')) 

s.close()
