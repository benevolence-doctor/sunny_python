#!/usr/bin/python
#coding:utf8
def counter(start_at=0):
    count = [start_at]
    def incr():        
        count[0]+=1
        return count[0]
    return incr      

count = counter(5)
for i in range(10):
    print count(),
count = counter(100)
print count()       #101
