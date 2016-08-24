# -*- coding:utf-8 -*-
import zmq


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5557")


for request in range(1, 11):
    socket.send(b"hello")
    message = socket.recv()
    print ("Received reply %s [%s]" % (request, message))
