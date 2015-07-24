#!/usr/bin/python
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
#    return imglist      
    x = 0  
    for imgurl in imglist:  
        urllib.urlretrieve(imgurl,'%s.jpg' % x)  
        x = x + 1     

html = getHtml("http://www.taobao.com/")
print getImg(html)

