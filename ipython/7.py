#!/usr/bin/python
from functools import  partial
RECORD_SIZE = 32
with open('/etc/passwd', 'rb') as f:
    #records = iter(f.read(32),b'')
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        
        with open('/tmp/'+str(f.tell()), 'wb') as sf:
            sf.write(r)
            print str(f.tell())
