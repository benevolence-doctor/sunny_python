#!/usr/bin/python
import webbrowser as web 
import time
import os
file = open("aa.txt")
for line in file:
   web.open_new_tab(line)
   time.sleep(3)
   os.system('taskkill /F /IM iexplore.exe')
   print line
