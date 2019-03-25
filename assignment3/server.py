import socketserver
import argparse
from os.path import exists

HOST = ''
PORT = ''
directory = ''

class MyTcpHandler(socketserver.BaseRequestHandler):
	def handle(self):
		data_transferred = 0
		print('[%s]  connected' %self.client_address[0])
		
		filename = self.request.recv(1024)
		filename = filename.decode()
		
		if not exists(filename) :
			return # handle()	

		print('file [%s] transfer start' %filename)
		with open('./'+directory+'/'+filename, 'rb') as f:
			try:
				data = f.read(1024)
				while data:
					data_transferred += self.request.send(data)
					data = f.read(1024)
			except Exception as e:
				print(e)
			print('transfer complete.\nfile name : %s\nsize : %d'%(filename, data_transferred))

def runServer():
	print('++++++file server start +++++++++')
	print("+++ file server end ? 'ctrl+c' press")

	try:	
		server = socketserver.TCPServer((HOST,PORT),MyTcpHandler)
		server.serve_forever()
	except KeyboardInterrupt:
		print('+++++file server end.++++++++')

parser = argparse.ArgumentParser(description= "Echo server -p port -d directory")

parser.add_argument('-p', help = "PORT", required = True)
parser.add_argument('-d', help = "directory_name", required = True)
args=parser.parse_args()
directory = args.d
PORT= int(args.p)
runServer()
