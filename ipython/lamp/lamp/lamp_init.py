#!/bin/env python
#-*- coding:utf-8 -*-

'''
 LAMP Install
'''

from fabric.api import cd, run, get, put, sudo, settings, hide, execute

class Mysql(object):
    def __init__(self, softname, installdir):
        self.softname = softname
        self.installdir = installdir

    def mysql_install(self):
        put('/root/fabric/soft/%s'%self.softname, '/tmp/%s'%self.softname)
        sudo("cd /tmp;tar zxvf %s"%self.softname)
        dirname = '.'.join(self.softname.split('.')[0:3])
        with cd('/tmp/%s'%dirname):
	    sudo("./configure --prefix=%s --localstatedir=%s/data --with-extra-charsets=complex \
		--enable-thread-safe-client --enable-local-infile  --enable-assembler --with-big-tables \
		--with-plugins=innobase,federated"%(self.installdir, self.installdir))
            sudo('make')
            sudo('make install')
	sudo("rm -rf /tmp/%s; rm -rf /tmp/%s" % (dirname, self.softname))

    def mysql_init(self):
	with settings(
	    hide('warnings', 'stderr'),
	    warn_only=True
	):
	    user_status = run("id mysql")
	    if user_status.succeeded:
		print "user mysql already exits. "
	    else:
		run("useradd mysql") 
	    cmdcheck = run('lsof -i:3306 &>/dev/null')
	    pidcheck = run('ps aux | grep mysqld | grep -v grep')
	    if cmdcheck.succeeded and pidcheck.succeeded:
		run("%s/bin/mysqladmin shutdown" % self.installdir)
		run("mkdir -p %s/etc"%self.installdir)
		run("cp -arf %s/share/mysql/my-medium.cnf %s/etc/my.cnf"% (self.installdir, self.installdir))
		run("%s/bin/mysql_install_db --datadir=/home/mysql/data --user=mysql "% self.installdir)
		with cd("%s" % self.installdir):
		    run('chgrp -R mysql .')
		    run('echo "%s/bin/mysqld_safe --defaults-file=%s/etc/my.cnf --datadir=/home/mysql/data \
			 --user=mysql &" >> /etc/rc.local' % (self.installdir, self.installdir))
	    else:
		run("mkdir -p %s/etc"%self.installdir)
		run("cp -arf %s/share/mysql/my-medium.cnf %s/etc/my.cnf" % (self.installdir, self.installdir))
		run("%s/bin/mysql_install_db --datadir=/home/mysql/data --user=mysql "% self.installdir)
		with cd("%s" % self.installdir):
		    run('chgrp -R mysql .')
		    run('echo "%s/bin/mysqld_safe --defaults-file=%s/etc/my.cnf --datadir=/home/mysql/data \
		    --user=mysql &" >> /etc/rc.local' % (self.installdir, self.installdir))	
	    
    def mysql_start(self):
	with settings(
            hide('warnings', 'stderr'),
            warn_only=True
        ):
	    cmdcheck = run('lsof -i:3306 &>/dev/null')
	    pidcheck = run('ps aux | grep mysqld | grep -v grep')
	    if cmdcheck.succeeded and pidcheck.succeeded:
		print "mysql server is running ...... "
	    else:
		run('nohup %s/bin/mysqld_safe --defaults-file=%s/etc/my.cnf --datadir=/home/mysql/data --user=mysql 1>&2 >/dev/null &' %(self.installdir, self.installdir),  pty=False)
    def mysql_stop(self):
	with settings(
            hide('warnings', 'stderr'),
            warn_only=True
        ):
	    cmdcheck = run('lsof -i:3306 &>/dev/null')
	    pidcheck = run('ps aux | grep mysqld | grep -v grep')
	    if cmdcheck.succeeded and pidcheck.succeeded:
		run("%s/bin/mysqladmin shutdown"%self.installdir)
	    else:
		print "mysql serice is already stoped ...... " 
    
class Apache(object):
    def __init__(self, softname, installdir):
        self.softname = softname
        self.installdir = installdir

    def apache_install(self):
        put("/root/fabric/soft/%s"%self.softname, '/tmp/%s'%self.softname)
        run("cd /tmp; tar zxvf %s"%self.softname)
        dirname = '.'.join(self.softname.split('.')[0:3])
        with cd("/tmp/%s"%dirname):
            run('useradd htdocs -s /sbin/nologin')
            run("./configure --prefix=%s --enable-dav --enable-dav-fs --enable-so \
		--enable-modules=most --enable-mods-shared=all --enable-info --enable-rewrite --enable-deflate --enable-ssl"%self.installdir)
            run('make')
            run('make install')

    def apache_init(self):
        run("sed -i 's/User daemon/User htdocs/; s/Group daemon/Group htdocs/'  %s/conf/httpd.conf"% self.installdir)
	run('echo "%s/bin/apachectl" >> /etc/rc.local' % self.installdir)

    def apache_start(self):
	with settings(
            hide('warnings', 'stderr'),
            warn_only=True
        ):
            cmdcheck = run('lsof -i:80 &>/dev/null')
            pidcheck = run('ps aux | grep httpd | grep -v grep')
            if cmdcheck.succeeded and pidcheck.succeeded:
		print "http service is already running ...... "
	    else:
		run("%s/bin/apachectl start"%self.installdir)

    def apache_stop(self):
	with settings(
            hide('warnings', 'stderr'),
            warn_only=True
        ):
            cmdcheck = run('lsof -i:80 &>/dev/null')
            pidcheck = run('ps aux | grep httpd | grep -v grep')
            if cmdcheck.succeeded and pidcheck.succeeded:
		run("%s/bin/apachectl stop"%self.installdir)
	    else:
		print "http service is already stoped ...... "

class Php(object):
    def __init__(self, softname, installdir):
	self.softname = softname
	self.installdir = installdir
	
    def php_install(self):
	put("/root/fabric/soft/epel-release-5-4.noarch.rpm", "/tmp/")
	run("rpm -ivh /tmp/epel-release-5-4.noarch.rpm")
	run("yum clean")
	run("yum -y install libgcrypt libgcrypt-devel libjpeg libjpeg-devel libpng libpng-devel  libxslt libxslt-devel freetype freetype-devel gd \
	    freetds  freetds-devel libmcrypt libmcrypt-devel mysql mysql-libs mysql-devel")
	put("/root/fabric/soft/%s"%self.softname, '/tmp/%s'%self.softname)
	run("cd /tmp; tar zxvf %s"%self.softname)
	dirname = '.'.join(self.softname.split('.')[0:3])
	with cd("/tmp/%s"%dirname):
	    run("./configure --prefix=%s --with-apxs2=/usr/local/apache/bin/apxs --with-iconv --with-openssl  --with-mysql=/usr/local/mysql5/ \
		    --with-curl --with-libxml-dir --with-libexpat-dir --enable-soap --with-xsl --with-gd --with-jpeg-dir --with-zlib --with-png-dir \
		    --with-freetype-dir --with-xmlrpc --with-mcrypt --enable-sockets  --enable-mbstring --enable-static  --enable-pcntl --with-mssql \
		    --enable-maintainer-zts --enable-inline-optimization --enable-wddx --enable-zip --enable-calendar --enable-bcmath --enable-soap \
		    --with-openssl --disable-ipv6 --disable-debug --disable-maintainer-zts --disable-fileinfo"%self.installdir)
	    run('make')
	    run('make install')
	    run("cp php.ini-dist %s/lib/php.ini" %self.installdir)
	    run("sed -i '/AddType application\/x-gzip .gz .tgz/a  AddType application/x-httpd-php .php AddType \
		application/x-httpd-php-source .phps' /usr/local/apache/conf/httpd.conf")
	    run('echo -e "<?php phpinfo() ?>"  >> /usr/local/apache/htdocs/test.php')
	
