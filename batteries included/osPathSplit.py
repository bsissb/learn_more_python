import os
import sys

if __name__ == '__main__':
    print os.path.realpath(sys.argv[0])
    print os.path.split(os.path.realpath(sys.argv[0]))
    print os.path.split(os.path.realpath(sys.argv[0]))[0]