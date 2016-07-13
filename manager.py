#!/usr/bin/env python
"""
    Description:

    Location:

    Configuration:

"""

from __future__ import print_function

from twisted.internet import protocol
from twisted.internet import task
from twisted.internet.defer import Deferred
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver

import sys

import threading

# CONTROLLER_IP = "localhost"
SERVICE_PORT = 7777



class MessageSender(LineReceiver):

    def connectionMade(self):
        # send the message
        # print("in message connection made", self.factory.message)

        self.transport.write(self.factory.message)

    def dataReceived(self, send_time):
        print(send_time)
        # close the connection
        self.transport.loseConnection()



class StreamFactory(ClientFactory):
    protocol = MessageSender

    def __init__(self, _message):
        self.done = Deferred()
        self.message = _message


    def clientConnectionFailed(self, connector, reason):
        # print('connection failed:', reason.getErrorMessage())
        self.done.errback(reason)


    def clientConnectionLost(self, connector, reason):
        # print('connection lost:', reason.getErrorMessage())
        self.done.callback(None)


def main(reactor, senderIP, destIP, n_files):
    # print( "sender IP is  ", senderIP)
    # print ("destination IP is ", destIP)
    # print("number of files = ", n_files)

    message = destIP + " , " + str(n_files)
    factory = StreamFactory(message)
    reactor.connectTCP(senderIP, SERVICE_PORT, factory)
    return factory.done


if __name__ == '__main__':
    task.react(main, sys.argv[1:])
