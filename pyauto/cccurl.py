#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import sys
import pycurl
reload(sys)
sys.setdefaultencoding( "utf-8" )
URL="http://cm12.c110.storage.bokecc.com/crossdomain.xml"
c = pycurl.Curl()
c.setopt(pycurl.URL, URL)
                
indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt", "wb")
c.setopt(pycurl.WRITEHEADER, indexfile)
c.setopt(pycurl.WRITEDATA, indexfile)
try:
    c.perform()
except Exception,e:
    print "connecion error:"+str(e)
    indexfile.close()
    c.close()
    sys.exit()

HTTP_CODE =  c.getinfo(c.HTTP_CODE)
print "HTTP״̬�룺%s" %(HTTP_CODE)

indexfile.close()
c.close()
