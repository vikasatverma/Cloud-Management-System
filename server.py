#!/usr/bin/python3           # This is server.py file
import socket                                         

def fibonacci(n, f0=0, f1=1):
	if n == 0:
		return f0
	while n > 1:
		f0, f1 = f1, f0 + f1
		n -= 1
	return f1



# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 
serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
port = 30000 #port to accept requests from load-balancer                                          
serversocket.bind(("", port))                                  
serversocket.listen(2000)                                           
clientsocket,addr = serversocket.accept()

while True:
	msg = clientsocket.recv(4)
	replySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = "192.168.1.10"  #Client
	port = 10000
	replySocket.connect((host, port))
	#print(msg.decode('ascii')+"\r\n")
	val = int(msg.decode('ascii'))
	num = fibonacci(val)
	result=0
	while num > 0:
		rem = num % 10
		result = result + rem
		num = int(int(num)//10)
	replySocket.send((str(result)).encode('ascii'))
	replySocket.close()

