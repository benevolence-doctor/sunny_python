#encoding=utf-8
import urllib2

#mp3file = urllib2.urlopen("http://music.baidu.com/data/music/file?link=http://zhangmenshiting.baidu.com/data2/music/118358164/14385500158400128.mp3?xcode=0c4914c4cd6ba3f9e639d47ca22d5ba031ba6b5fb13a98ae&song_id=14385500")
#output = open('/tmp/test.mp3', 'wb')
#
#output.write(mp3file.read())
#output.close()
#print "文件下载完毕"
jpg = urllib2.urlopen('http://s0.hao123img.com/res/ecom/pianyi-0422.jpg')
with open('/tmp/a.jpg','w') as f:
    f.write(jpg.read())
