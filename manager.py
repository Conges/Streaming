#!/usr/bin/env python
"""
    Description:

    Location:

    Configuration:

"""

from __future__ import print_function

from twisted.internet import task
from twisted.internet.defer import Deferred
from twisted.internet import protocol
from twisted.protocols.basic import LineReceiver

import sys

import threading

# CONTROLLER_IP = "localhost"
SERVICE_PORT = 7777

src_ip = "localhost"
dst_ip = "localhost"
nmr_files = 2

def new_connection(x):
    print("Enter sender IP:")
    src_ip = sys.stdin.readline()
    src_ip = src_ip.rstrip()

    print ("Enter destination IP:")
    dst_ip = sys.stdin.readline()
    dst_ip = dst_ip.rstrip()

    print ("Enter number of files:")
    nmr_files = int(sys.stdin.readline().rstrip())

    message = dst_ip + " , " + str(nmr_files)
    sendMessage(src_ip, SERVICE_PORT, message, x)


class MessageSender(protocol.Protocol):
    def __init__(self, message, x):
        print("in message sender inintalizdrs")
        self.message = message
        print(x)
        self.x = x

    def connectionMade(self):
        # send the message
        print("in message conncetion made")
        self.transport.write(self.message)
        # close the connection
        self.transport.loseConnection()

    def connectionLost(self, reason):
        print("connection lost")
        new_connection(self.x)


def sendMessage(host, port, message, reactor):
    cc = protocol.ClientCreator(reactor, MessageSender, message, reactor)
    cc.connectTCP(host, port)


def main(reactor):
    new_connection(reactor)
    reactor.run()
    return


if __name__ == '__main__':
    task.react(main)
