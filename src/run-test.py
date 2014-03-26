#!/usr/bin/python
#
# Evaluate and execute all of the python files passed as argument
#

import sys

# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)

for i in range(1, len(sys.argv)):
    f = open(sys.argv[i])
    exec(f.read())
