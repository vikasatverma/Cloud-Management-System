import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = "192.168.1.11"  #Load balancer                         
port = 20000 # registeration port

s.connect((host, port))                               

s.send(("Register Me!!").encode('ascii'))

s.close()
