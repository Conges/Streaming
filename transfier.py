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
        self.strart_num = 459
        self.dst_ip = "192.168.1.4"
        self.dst_user = "ubuntu"
        self.dst_path = "ftp_files/"
        self.src_path = ""
        self.total_number_files = 0
        self.successful_sent_files = 0

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

        # print("rv = %s" %rv)
        # if rv == 0:
        #     print("adding")
        #     self.successful_sent_files += 1
        #     print("after adding successful is %s" % self.successful_sent_files)

        # self.globallock.release()

    def get_list_of_files(self, count):
        files = []
        for i in xrange(0, count):
            files.append(str(self.strart_num) + ".mp4")
        return files

    def set_info(self, dst, count):
        self.dst_ip = dst
        self.total_number_files = count

    def send_files(self, dst, count):
        self.set_info(dst, count)
        files = self.get_list_of_files(count)
        print files
        # self.successful_sent_files = 0
        p = Pool()
        p.map(self.processfile, files)
        p.close()
        p.join()
        # print("successful is %s"%self.successful_sent_files)
        # success_rate = int(100 * (self.successful_sent_files / self.total_number_files))
        # return success_rate


# def main(argv):
    # ss = StreamSender()
    # ss.send_files("192.168.1.4", 2)

# if __name__ == '__main__':
#     main(sys.argv)
