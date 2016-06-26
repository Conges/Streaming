# http://stackoverflow.com/questions/9554544/python-running-command-line-tools-in-parallel

import sys
import subprocess
from multiprocessing import Pool, Lock
import copy_reg
import types

def _pickle_method(m):
    if m.im_self is None:
        return getattr, (m.im_class, m.im_func.func_name)
    else:
        return getattr, (m.im_self, m.im_func.func_name)

copy_reg.pickle(types.MethodType, _pickle_method)

class StreamSender:
    def __init__(self):
        # self.globallock = Lock()
        self.strart_num = 454
        self.dst_ip = "192.168.1.4"
        self.dst_user = "gui"
        self.dst_path = "ftp_files/"
        self.src_path = ""

    def processfile(self, name):
        """Adds copyright notice to the file.

        Arguments:
        name -- file to modify
        """

        # parm = src_path + name + " " + dst_user + "@" + dst_ip + ":" + dst_path
        # print parm
        args = ['scp' ,self.src_path + name , self.dst_user + "@" + self.dst_ip + ":" + self.dst_path]
        # args = ['echo', name]

        rv = subprocess.call(args)

        # self.globallock.acquire()
        # if rv != 0:
        #     print "Error when processing file '{}'".name
        # self.globallock.release()

    def get_list_of_files(self, count):
        files = []
        for i in xrange(0, count):
            files.append(str(self.strart_num+i) + ".mp4")
        return files

    def set_info(self, dst):
        self.dst_ip = dst

    def send_files(self, dst, count):
        self.set_info(dst)

        files = self.get_list_of_files(count)
        print files
        p = Pool()
        p.map(self.processfile, files)
        p.close()
        p.join()


# def main(argv):
    # ss = StreamSender()
    # ss.send_files("192.168.1.4", 2)

# if __name__ == '__main__':
#     main(sys.argv)
