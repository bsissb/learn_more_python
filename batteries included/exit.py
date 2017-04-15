# coding:utf-8
import sys

def exitfunc(value):
    print value
    sys.exit(0)

print "h"


try:
    sys.exit(1)
except SystemError,value:
    exitfunc(value)