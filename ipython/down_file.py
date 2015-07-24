#!/usr/bin/python
#encoding=utf-8
import urllib2

down_file = 'you_down_file.html'
url = 'http://s0.hao123img.com/res/ecom/pianyi-0422.jpg'
response = urllib2.urlopen(url)


fh = open(down_file, 'w')
#在本地创建文件you_down_file.html
fh.write(response.read()) 

fh.close()

#以下方式效果一样

#with open(down_file, 'w')  as f:
#    f.write(response.read())        
