#codint = utf-8
import os
import SocketServer
import threading
import socket

SERVER_HOST = 'localhost'
SERVER_PORT = 0
BUF_SIZE = 1024

def client(ip, port, msg):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(msg)
        resp = sock.recv(BUF_SIZE)
        print "Client received: %s" % resp
    finally:
        sock.close()

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        current_thread = threading.current_thread()
        resp = "%s : %s" % (current_thread.name, data)
        self.request.sendall(resp)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):

    pass

if __name__ == '__main__':
    server = ThreadedTCPServer((SERVER_HOST, SERVER_PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    print "Server loop running on thread: %s" % server_thread.name

    client(ip, port, "Hello from client1")
    client(ip, port, "Hello from client2")
    client(ip, port, "Hello from client3")

    server.shutdown()
