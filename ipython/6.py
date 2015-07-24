#!/usr/bin/python
from functools import partial
def sum(a,b):
    return a+b 
for i in xrange(10):
    print i
#    test=iter(sum(i,1),5)
    test=iter(partial(sum,i,1),5)
    print i,test.next()
