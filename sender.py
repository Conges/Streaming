#!/usr/bin/env python

"""
    Description:

    Location:

    Configuration:

"""


from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor

from pprint import pprint
import time
import decimal
from transfier import *

CONTROLLER_PORT = 7777

class StreamServer(Protocol):

    def dataReceived(self, data):
        data = data.split(' , ')
        print data

        ss = StreamSender()
        st_time = time.time()

        ss.send_files(data[0], int(data[1]))

        send_time = time.time() - st_time
        TWOPLACES = decimal.Decimal(10) ** -2
        send_time = str(decimal.Decimal(send_time).quantize(TWOPLACES))

        print("--- %s seconds ---" % send_time)
        self.transport.write(send_time)


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
