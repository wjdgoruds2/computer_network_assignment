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
		print('from : ',addr,', ', recvData.decode('utf-8'))

port ='' 
host =''
parser = argparse.ArgumentParser(description="Echo client.py -i hostid -p port")
parser.add_argument('-i', help="hostid", required=True)
parser.add_argument('-p', help = "PORT", required = True)
args=parser.parse_args()
port= int(args.p)
host=args.i

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((host,port))
addr = (host, port)

sender = threading.Thread(target=send, args=(clientSock,))
receiver = threading.Thread(target=receive, args=(clientSock,))

sender.start()
receiver.start()

while True:
	time.sleep(1)
	pass
