#!/usr/bin/python

import sys

print("len(sys.argv) = ", len(sys.argv))
print('sys.arg[]:', str(sys.argv))
for index, value in enumerate(sys.argv):
    print("argv[", index, "] = <", value, ">")

# if len(sys.argv) != 2:
#     print("Usage: ", sys.argv[0], " ROOT-FILE")
#     sys.exit(1)
# else:
#     print (sys.argv[1]);

    
