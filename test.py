import sys

print("press enter")
while True:
        line = sys.stdin.readline()
        if(line == ''):
            break;
        print("Enter sender IP:")
        src_ip= sys.stdin.readline()

        print ("Enter destination IP:")
        dst_ip = sys.stdin.readline()

        print ("Enter number of files:")
        nmr_files = int(sys.stdin.readline())

print(src_ip)
print("test")
