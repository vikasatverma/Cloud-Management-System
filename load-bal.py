#!/usr/bin/python3           # This is server.py file
import socket                                         
import _thread

servers=[]
DictServerSockets=[]

def connectToServer(host):
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	port = 30000 #port to forward requests to servers
	serversocket.connect((host, port)) 
	DictServerSockets.append(serversocket)                              
                                 


def RegisterNewServer():
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	port = 20000
	serversocket.bind(("", port))
	serversocket.listen(5)
	
	while True:
		clientsocket,addr = serversocket.accept()
		print("Registering "+addr[0])
		servers.append(addr[0])
		print(servers)
		clientsocket.close()
		connectToServer(addr[0])

_thread.start_new_thread(RegisterNewServer,())



# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)


port = 9999 #port to accept requests from Client                                          

# bind to the port
serversocket.bind(("", port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

clientsocket,addr = serversocket.accept()      

serverTurn=0
while True:
   # establish a connection
	msg = clientsocket.recv(1024)
	print(msg.decode('ascii')+"\r\n")
	serverTurn = serverTurn+1
	serverTurn = serverTurn % len(DictServerSockets)
	print("serverTurn: %s"%serverTurn)
	DictServerSockets[serverTurn].send(msg)
