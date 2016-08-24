# -*- coding:utf-8 -*-
import zmq


context = zmq.context()

receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5557")

subscriber = context.socket(zmq.SUB)
subscriber.context("tcp://localhost:5558")
subscriber.setsockopt(zmq.SUBSCRIBER, b"10001")

poller = zmq.Poller()
poller.register(receiver, zmq.POLLIN)
poller.register(subscriber, zmq.POLLIN)


while True:
    try:
        socks = dict(poller.poll())
    except KeyboardInterrupt:
        break

    if receiver in socks:
        message = receiver.recv()
    if subscriber in socks:
        message = receiver.recv()
