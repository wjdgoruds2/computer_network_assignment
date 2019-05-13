import os

import socket

import argparse

import struct



#python3 sniffer.py -i ens33 lo

ETH_P_ALL = 0x0003

ETH_SIZE = 14

IP_SIZE = 34

#ETH_TYPE = 1

COUNT = 3



def dumpcode(buf):

   print("%7s"% "offset ", end='')



   for i in range(0, 16):

      print("%02x " % i, end='')



      if not (i%16-7):

         print("- ", end='')



   print("")



   for i in range(0, len(buf)):

      if not i%16:

         print("0x%04x" % i, end= ' ')



      print("%02x" % buf[i], end= ' ')



      if not (i % 16 - 7):

         print("- ", end='')



      if not (i % 16 - 15):

         print("")



   print("")



def make_ethernet_header(raw_data):

   ether = struct.unpack('!6B6BH',raw_data)

   

   global ETH_TYPE

   if ether[12] == 2048 : 

      ETH_TYPE = 1

      return { 'dst' : '%02x:%02x:%02x:%02x:%02x:%02x' % ether[:6],

          'src' : '%02x:%02x:%02x:%02x:%02x:%02x' % ether[6:12],

          'ether_type' : ether[12] }

   else :

      ETH_TYPE = 0



def make_ip_header(raw_data):

   ip = struct.unpack('!BBHHHBBH4B4B',raw_data)

   return { 'Version' : int(bin(ip[0])[2:5],2),

       'HeadLength' : int(bin(ip[0])[5:],2),

       'Tos' : ip[1],

       'TotalLength' : ip[2],

       'Id' : ip[3],

       'Flag' : int(format(ip[4],'b')[:2],2),

       'offset' : int(format(ip[4],'b')[2:],2),

       'ttl' : ip[5],

       'protocol' : ip[6],

       'checksum' : ip[7],

       'src' : '%d.%d.%d.%d' % ip[8:12],

       'dst' : '%d.%d.%d.%d' % ip[12:16] }





def sniffing(nic):

   if os.name == 'nt':

      address_familiy = socket.AF_INET

      protocol_type = socket.IPPROTO_IP

   else:

      address_familiy = socket.AF_PACKET

      protocol_type = socket.ntohs(ETH_P_ALL)

   with socket.socket(address_familiy, socket.SOCK_RAW, protocol_type) as sniffe_sock:

      sniffe_sock.bind((nic, 0))

      if os.name == 'nt':

         sniffe_sock.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)

         sniffe_sock.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)

      



      data, _ = sniffe_sock.recvfrom(65535)

      ethernet_header = make_ethernet_header(data[:ETH_SIZE])

      ip_header = make_ip_header(data[ETH_SIZE:IP_SIZE])



      if ETH_TYPE == 1 :



         print('[2] IP_PACKET-------------------------------------------')

         print(" ")



         print('Ethernet Header')

         for item in ethernet_header.items():

            print('[{0}] : {1}'.format(item[0],item[1]))

         print(" ")



         print('IP Header')

         for item in ip_header.items():

            print('[{0}] : {1}'.format(item[0],item[1]))

         print(" ")



         print('raw data')

         dumpcode(data)



      if os.name == 'nt':

         sniffe_sock.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)





if __name__ == '__main__':

   parser = argparse.ArgumentParser(description='This is a simpe packet sniffer')

   parser.add_argument('-i', type=str, required=True, metavar='NIC name', help='NIC name')

   args = parser.parse_args()



   while COUNT :

      sniffing(args.i)

      COUNT = COUNT - 1 
