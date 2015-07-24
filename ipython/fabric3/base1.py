#!/bin/env python
#-*- coding:utf8 -*-

from fabric.api import *

env.hosts = ['192.168.10.34', '192.168.10.10', '192.168.10.11', '192.168.10.200', '192.168.10.34']


def test_cd():
	with cd('/tmp'):
		run('touch a')
		run('touch b')

def test_hide():
	with hide('running', 'stdout', 'stderr'):
		with cd('/tmp'):
			run('touch a')
			run('touch b')

def test_settings():
	with settings(
		hide('warnings', 'stdout', 'stderr'),
		warn_only=True,
		host_string='192.168.10.10'
	):
		print env.host_string
		host_string='192.168.10.100'
		print env.host_string
	
def test_show():
	with show('running', 'stdout', 'stderr'):
		with cd('/tmp'):
			run('touch c')
			run('touch d')


def test_path():
	run('echo $PATH')
	with path('/root/sbin',behavior='replace'):
		run('echo $PATH')

def test_prefix():
	with prefix('cd /tmp'):
		run('touch a')
		run('touch b')

