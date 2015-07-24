#!/bin/env python
#-*- coding:utf8 -*-

from fabric.api import *
from getpass import getpass
env.dedupe_hosts=False
env.exclude_hosts = ['192.168.10.200']
env.skip_bad_hosts = True
env.timeout = 1
env.password = '123456'

env.roledefs = {'web': ['192.168.10.34', '192.168.10.8' ],
				'db' : ['192.168.10.34', '192.168.10.8', '192.168.10.10', '192.168.10.11', '192.168.10.200', '192.168.10.181', '192.168.10.182']
				}

#@hosts('192.168.10.34', '192.168.10.8')
@roles('db', 'web')
def host_type():
	run('uname -s')

@runs_once
def get_user_passwd(user):
	passwd = prompt('Enter a new password for user %s:' % user)
	if passwd:
		return passwd

@roles('db')
def change_pass(user):
	passwd = get_user_passwd(user)
	run("echo '%s' | passwd --stdin %s" %(passwd, user))

@serial
#@task
#@parallel(pool_size=10)
@roles('db')
def load():
	run('uptime')

def remote_require():
	if not require('parallel'):
		print 'key is not exist'

@hosts('192.168.10.34')
def remote_put():
	put('/root/ipython-1.2.1.tar.gz', '/tmp/')

@hosts('192.168.10.34')
def remote_get():
	get('/tmp/ipython-1.2.1.tar.gz', '/tmp/')

@hosts('192.168.10.34')
def remote_local():
	local('uptime')

@hosts('192.168.10.34')
def remote_reboot():
	reboot(wait=10)


@hosts('192.168.10.34')
def remote_open_shell():
	open_shell('uptime')


def task1(dirname):
	run('mkdir -p /tmp/%s'%dirname)

def task2(dirname):
	run('mkdir -p /tmp/%s'%dirname)

@hosts('192.168.10.34')
def dotask():
	execute(task1, 'fabrictest1')
	execute(task2, 'fabrictest2')


