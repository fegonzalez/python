#!/usr/bin/python

import sys

print("len(sys.argv) = ", len(sys.argv))
print('sys.arg[]:', str(sys.argv))
for index, value in enumerate(sys.argv):
    print("argv[", index, "] = <", value, ">")
