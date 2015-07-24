#!/bin/env python
#-*- coding:utf-8 -*-

'''
install LAMP function
'''

from fabric.api import run, parallel, env
from lamp import lamp_init

env.password = 'berlin493'
env.hosts=[]

@parallel
def mysql_install():
    mysql = lamp_init.Mysql('mysql-5.1.45.tar.gz', '/usr/local/mysql5')
    mysql.mysql_install()

def mysql_init():
    mysql = lamp_init.Mysql('mysql-5.1.45.tar.gz', '/usr/local/mysql5')
    mysql.mysql_init()

def mysql_start():
    mysql = lamp_init.Mysql('mysql-5.1.45.tar.gz', '/usr/local/mysql5')
    mysql.mysql_start()

def mysql_stop():
    mysql = lamp_init.Mysql('mysql-5.1.45.tar.gz', '/usr/local/mysql5')
    mysql.mysql_stop()

def http_install():
    http = lamp_init.Apache('httpd-2.2.14.tar.gz', '/usr/local/apache')
    http.apache_install()

def http_init():
    http = lamp_init.Apache('httpd-2.2.14.tar.gz', '/usr/local/apache')
    http.apache_init()

def http_start():
    http = lamp_init.Apache('httpd-2.2.14.tar.gz', '/usr/local/apache')
    http.apache_start()

def http_stop():
    http = lamp_init.Apache('httpd-2.2.14.tar.gz', '/usr/local/apache')
    http.apache_stop()

def php_install():
    php = lamp_init.Php('php-5.4.29.tar.gz', '/usr/local/php')
    php.php_install()
