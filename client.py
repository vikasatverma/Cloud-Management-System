#!/usr/bin/python3           # This is client.py file
from random import random
from random import seed
from queue import Queue
import socket
import time
import _thread
import sys

q=Queue(maxsize=10)

def acceptReply():
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	port = 10000
	serversocket.bind(("", port))
	serversocket.listen(5)
	
	while True:
		clientsocket,addr = serversocket.accept()
		msg = clientsocket.recv(1024)
		#print("reply:" +msg.decode('ascii')+"\r\n")
		clientsocket.close()

_thread.start_new_thread(acceptReply,())


def varySpeed():
	while(1):
		q.put(input())
		
_thread.start_new_thread(varySpeed,())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = "192.168.1.11"  #Load balancer                         

port = 9999

s.connect((host, port)) 
timer=1                              

#for i in list(range(1000)):
while True:
	time.sleep(timer)
	while(not q.empty()):
		try:
			speed=float(q.get())
			if(speed<0.0001):
				pass
			else:
				timer=speed
		except Exception:
				pass
		print("current gap btw consecutive req: %s"%timer)
	val = int(random()*10000)
	#print("sending %s"%val)
	s.send((str(val)).encode('ascii')) 
s.close()
