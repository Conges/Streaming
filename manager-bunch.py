# http://stackoverflow.com/questions/9554544/python-running-command-line-tools-in-parallel

import sys
from multiprocessing import Pool, Lock
import copy_reg
import types
from subprocess import Popen, PIPE

def _pickle_method(m):
    if m.im_self is None:
        return getattr, (m.im_class, m.im_func.func_name)
    else:
        return getattr, (m.im_self, m.im_func.func_name)

copy_reg.pickle(types.MethodType, _pickle_method)


class ManagerBunch:
    def __init__(self, _n_files):
        self.n_files = _n_files
        self.pairs = []

    def processfile(self, thread_id):
        # print("in process file with id = ", thread_id)
        # print "in files = ", self.n_files
        p = Popen(['python', "manager.py", self.pairs[thread_id][0], self.pairs[thread_id][1], str(self.n_files) ], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()
        rc = p.returncode
        return output



    def start(self, _pairs):
        self.pairs = _pairs
        p = Pool()
        values = p.map(self.processfile, range(len(self.pairs)))
        # print(values)
        overall_time = 0
        for x in values:
            # print(x.rstrip())
            try:
                x = float(x.rstrip())
            except ValueError:
                overall_time = -10 ** 10
                continue
            overall_time += x

        overall_time = int(overall_time)
        print(overall_time)
        p.close()
        p.join()


def get_pairs(in_file):
    pairs = []
    with open(in_file) as file_obj:
        for line in file_obj:
            pairs.append((line.split()[0], line.split()[1]))
    return pairs

def main(argv):
    mb = ManagerBunch(argv[1])
    pairs = get_pairs("bunch-pairs.in")
    # print pairs
    mb.start(pairs)

if __name__ == '__main__':
    main(sys.argv)
