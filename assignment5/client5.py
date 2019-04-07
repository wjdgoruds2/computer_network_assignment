## client.py

import socket
import argparse
   

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Echo client -p port -i host")
    parser.add_argument('-p', help="port_number", required=True)
    parser.add_argument('-i', help="host_name", required=True)

    args = parser.parse_args()
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((args.i, int(args.p)))
    ## input으로 문자받아서 서버에게 보내기
    s.sendall(input('보낼 메세지 : ').encode('utf-8'))
    text = s.recv(1024)
    print(text.decode())
    s.close()
    

    
