#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib;
for deurl in open('url') : 
    decodedUrl = urllib.unquote(deurl)
    print decodedUrl,
