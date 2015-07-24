#!/usr/bin/python
import getpass
import sys
import telnetlib

HOST = "192.168.1.100"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ping 192.168.1.101\n")
#tn.write("exit\n")

print tn.read_all()
