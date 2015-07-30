#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import sys
import os
#for deurl in open('gjurl') : 
for deurl in open(sys.argv[1]) :     ###传参数类似shell脚本中的$1 $2
    decodedUrl = urllib.unquote(deurl)
    print decodedUrl,
