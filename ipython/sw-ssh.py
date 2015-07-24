#!/usr/bin/env python 
import paramiko   
username='phenix'  
password='pass'   
port=12
timeout=1
for line in open('/home/python/ip'):
    IP = line
    print IP
    paramiko.util.log_to_file('paramiko.log')          
    ssh=paramiko.SSHClient()                 
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())          
    ssh.connect(hostname = IP, port=port, username=username, password=password, timeout=timeout)          
    stdin,stdout,stderr=ssh.exec_command('ping 8.8.8.8') 
    print stdout.read()          
    ssh.close()  
