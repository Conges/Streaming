#!/usr/bin/env python

"""
    Description:

    Location:

    Configuration:

"""


from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor

from pprint import pprint
from transfier import *

CONTROLLER_PORT = 7777

class StreamServer(Protocol):

    def dataReceived(self, data):
        data = data.split(' , ')
        print data
        ss = StreamSender()
        ss.send_files(data[0], int(data[1]))


class MyFactory(Factory):
    def __init__(self):
        self.analyzer_map = dict()



def main():
    f = MyFactory()
    f.protocol = StreamServer
    reactor.listenTCP(CONTROLLER_PORT, f)
    reactor.run()
    # print f.analyzer_map

if __name__ == '__main__':
    main()
