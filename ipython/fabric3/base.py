#!/bin/env python
#-*- coding:utf8 -*-

from fabric.api import *
env.hosts = ['192.168.10.34', '192.168.10.10','192.168.10.200', '192.168.10.34','192.168.10.8']
env.dedupe_hosts=True
env.exclude_hosts = ['192.168.10.200']
env.skip_bad_hosts = True
env.timeout = 1

def hello1():
	print 'hello world'

def hello2(username):
	print 'hello , %s' %username

def hello3(username, age=40):
	print '%s is old %s' %(username, age)

def host_type():
	run('uname -s')
