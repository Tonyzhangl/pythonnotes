#coding=utf-8
import socket

def find_service_name():
    protocol_name = 'tcp'
    for port in [80, 25]:
        print "Port: %s => service name: %s" % (port, socket.getservbyport(port, protocol_name))

if __name__ == '__main__':
    find_service_name()
