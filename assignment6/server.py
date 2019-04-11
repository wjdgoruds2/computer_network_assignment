from socket import *
import threading
import time
import argparse
def send(sock):
	while True:
		sendData = input()
		sock.send(sendData.encode('utf-8'))

def receive(sock):
	while True:
		recvData = sock.recv(1024)
		print('from ', str(addr),', ',recvData.decode('utf-8'))

port ='' 
parser= argparse.ArgumentParser(description= "Echo server -p port")
parser.add_argument('-p', help = "PORT", required = True)
args= parser.parse_args()
port = int(args.p)

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('',port))
serverSock.listen(1)
connectionSock, addr = serverSock.accept()
print('Connected to : ',str(addr))
sender = threading.Thread(target=send, args = (connectionSock,))
receiver = threading.Thread(target=receive, args = (connectionSock,))

sender.start()
receiver.start()

while True:
	time.sleep(1)
	pass
