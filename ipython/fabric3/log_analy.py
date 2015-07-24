#!/bin/env python
#-*- coding:utf8 -*-

from operator import itemgetter, attrgetter
from itertools import groupby
import sys

def s_data(file):
    data = []
    tmp = []
    fp = open(file, 'r')
    for line in fp.readlines():
        ip = line.split()[0]
        url = line.split()[6]
        data.append([ip, url])
    data.sort(key=itemgetter(0, 1), reverse=True)
    return data

def work(data):
    res = []
    for key, items in groupby(data, itemgetter(0)):
	tmp1 = list(items)
	#print key, tmp1
	url = []
	ipc = len(tmp1)	
	tmp1.sort(key=itemgetter(1), reverse=True)	
	for subkey, subitems in groupby(tmp1, itemgetter(1)):
	    tmp2 = list(subitems)
	    #print subkey, len(tmp2)
	    url.append([subkey, len(tmp2)])
	url.sort(key=lambda x:x[1], reverse=True)
    	res.append([key,ipc, url[:1]])
	#print key, ipc, url[:1]
    return res

if __name__ == '__main__':
    data =  s_data(sys.argv[1])
    results = work(data)
    results.sort(key=lambda x:x[1], reverse=True)
    for result in results[:10]:
	print 'ip:%s, ip_count:%s, max_url:%s, max_url_count:%s' %(result[0], result[1], result[2][0][0], result[2][0][1])
