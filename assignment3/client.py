import socket
import argparse

HOST = ''
PORT = ''

def getFileFromServer(filename):
	data_transferred = 0

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
		sock.connect((HOST,PORT))
		sock.sendall(filename.encode())

		data = sock.recv(1024)
		if not data:
			print('file[%s]: error'%filename)
			return
	
		with open('./'+filename,'wb') as f:
			try:
				while data:
					f.write(data)
					data_transferred += len(data)
					data = sock.recv(1024)
			except Exception as e:
				print(e)

	print('file transfer complete.\nfilename : %s \nsize : %d' %(filename, data_transferred))


parser = argparse.ArgumentParser(description="Echo client.py -i hostid -p port -f filename")
parser.add_argument('-i', help="hostid", required=True)
parser.add_argument('-p', help="PORT", required=True)
parser.add_argument('-f', help="filename", required=True)

args=parser.parse_args()
PORT = int(args.p)
HOST = args.i
getFileFromServer(filename=args.f)
