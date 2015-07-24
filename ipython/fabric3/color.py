#!/bin/env python
#-*- coding:utf8 -*-

from fabric.colors import blue, red, green, yellow, white,cyan, magenta, black

def test_color():
	print blue('blue', bold=True)
	print red('red')
	print green('green')
	print yellow('yellow')
	print white('white')
	print cyan('cyan')
	print magenta('magenta')
	print black('black')
	
