#!/bin/bash 

from fabric.api import *
from fabric.colors import *
from fabric.network import *
from getpass import getpass
from crypt import crypt

env.user = 'root'
env.password = 'berlin493'
env.hosts = ['192.168.10.67', '192.168.10.68']
env.roledefs = {
		'web' : ['192.168.10.67'], 
		'db' : ['192.168.10.68']
	    }
env.passwords = {
		 '192.168.10.67' : 'berlin493', 
		 '192.168.10.68' : 'berlin493'
	    }

@parallel(pool_size=50)
def connect_status():
    with hide('running','stdout', 'stderr'):
			syn_recv = run('/usr/sbin/ss -atn state syn-recv sport = :http or sport = :https | wc -l')
			syn_sent = run('/usr/sbin/ss -atn state syn-sent sport = :http or sport = :https | wc -l')
			established = run('/usr/sbin/ss -atn state ESTABLISHED sport = :http or sport = :https | wc -l')
			fin_wait_1 = run('/usr/sbin/ss -atn state fin-wait-1 sport = :http or sport = :https | wc -l')
			fin_wait_2 = run('/usr/sbin/ss -atn state fin-wait-2 sport = :http or sport = :https | wc -l')
			time_wait = run('/usr/sbin/ss -atn state time-wait sport = :http or sport = :https | wc -l')
			close_wait = run('/usr/sbin/ss -atn state close-wait sport = :http or sport = :https | wc -l')
			closing = run('/usr/sbin/ss -atn state closing sport = :http or sport = :https | wc -l')
			closed = run('/usr/sbin/ss -atn state closed sport = :http or sport = :https | wc -l')
			last_ack = run('/usr/sbin/ss -atn state last-ack sport = :http or sport = :https | wc -l')
			print env.host
	print red('syn_recv:%s\n' %syn_recv + 'syn_sent:%s\n' %syn_sent + 'established:%s\n' %established + 'fin_wait_1:%s\n' %fin_wait_1 + 'fin_wait_2:%s\n' %fin_wait_2 \
		+ 'time_wait:%s\n' %time_wait + 'close_wait:%s\n' %close_wait + 'closing:%s\n' %closing + 'closed:%s\n' %closed + 'last_ack:%s\n' %last_ack)
	disconnect_all()
