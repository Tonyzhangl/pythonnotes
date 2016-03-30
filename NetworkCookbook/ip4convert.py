#coding=utf-8

import socket
from binascii import hexlify

def convert_ip4_address():
    ip_lists = ['127.0.0.1', '192.168.0.1']
    for ip in ip_lists:
        packed_ip = socket.inet_aton(ip)
        unpacked_ip = socket.inet_ntoa(packed_ip)
        print "IP Adress : %s => Packed : %s, Unpacked IP: %s" % (
            ip, hexlify(packed_ip), unpacked_ip
        )

if __name__ == '__main__':
    convert_ip4_address()
