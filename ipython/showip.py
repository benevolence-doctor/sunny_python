#!/usr/bin/env   python
#encoding: utf8
import BeautifulSoup
import StringIO
import pycurl
def showIP(ip):
        myurl = "http://www.ip138.com/ips1388.asp?ip="+str(ip)+"&action=2"
        html = StringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL,myurl) 
        c.setopt(pycurl.WRITEFUNCTION,html.write)
        c.setopt(pycurl.FOLLOWLOCATION,1)
        c.setopt(pycurl.MAXREDIRS,5)
        c.setopt(pycurl.TIMEOUT,300)
        c.setopt(pycurl.CONNECTTIMEOUT,60)
        ##设置uagent头
        c.setopt(pycurl.USERAGENT,"Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.0")
        c.perform()
        content = html.getvalue()
        ###解码然后编码为utf8，ingore参数是为了避免页面中的某些非法字符，导致异常
        content = content.decode('GB2312','ignore').encode('UTF-8')
        #print content
        #content = content.decode('GB2312').encode('UTF-8')
        soup = BeautifulSoup.BeautifulSoup(content)
        li = soup.find('li')
   #     print li
        ###组合为字符串
        shuchu= ip+"/32 "+li.string+" "+li.findNext('li').string
        ##输出编码
        print shuchu.encode('UTF-8')
        #print li
#f = open('ip.txt')
#for iplist in f:
# showIP(iplist.strip())
showIP('202.106.0.20')
