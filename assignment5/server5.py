## server.py

import socket
import argparse
import threading

## 클라이언트에게 받은 문자열을 뒤집어서 다시 클라이언트에게 보내줌
def socket_handler(conn):
        msg = conn.recv(1024)
        text = msg.decode()[::-1]
        conn.sendall(text.encode())
        conn.close()    

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Echo client -i host")
    parser.add_argument('-p', help="port_number", required=True)

    args = parser.parse_args()

    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(('',int(args.p)))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        print ('connect :',addr)
        threading.Thread(target=socket_handler(conn))
        print (addr[0],': closed')

    s.close()
