#coding=utf-8
import argparse
import xmlrpclib
import threading

from SimpleXMLRPCServer import SimpleXMLRPCServer

def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y


class ServerThread(threading.Thread):

    def __init__(self, server_addr):
        threading.Thread.__init__(self)
        self.server = SimpleXMLRPCServer(server_addr)
        self.server.register_multicall_functions()
        self.server.register_function(add, 'add')
        self.server.register_function(subtract, 'subtract')
        self.server.register_function(multiply, 'multiply')
        self.server.register_function(divide, 'divide')

    def run(self):
        self.server.serve_forever()

def run_server(host, port):
    server_addr = (host, port)
    server = ServerThread(server_addr)
    server.start()
    print "Server thread started, Testing the server..."

def run_client(host, port):
    proxy = xmlrpclib.ServerProxy("http://%s:%s/" % (host, port))
    multicall = xmlrpclib.MultiCall(proxy)
    multicall.add(7,3)
    multicall.subtract(7,3)
    multicall.multiply(7,3)
    multicall.divide(7,3)
    result = multicall()
    print "7+3:%d, 7-3:%d, 7*3:%d, 7/3:%d" % tuple(result)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Multithreaded multicall XMLRPCServer/Proxy")
    parser.add_argument("--host", action="store", dest="host", default='localhost')
    parser.add_argument("--port", action="store", dest="port", default=8000)
    given_args = parser.parse_args()
    host, port = given_args.host, given_args.port
    run_server(host, port)
    run_client(host, port)
