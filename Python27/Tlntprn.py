#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os
import telnetlib
import sys
import shutil
import time


path = '/home/pi/Python2/'
mpath = '/home/pi/Python2/Tmp/'
files = os.listdir(path)

try:
    txtfiles = filter(lambda x: x.endswith('.txt'), files) 
except:
    print 'Error filter.'
    sys.exit(0)

if not txtfiles:
    print 'No txt files.'
    sys.exit(0)
	
fil1nam = txtfiles[0]
fil1opn = open(txtfiles[0])
fil1cont = fil1opn.read()
fil1opn.close()
print path + fil1nam + '\n'
print fil1cont
shutil.move(path + fil1nam, mpath + fil1nam)

cutprn = chr(27) + chr(105)
tstatus = chr(29) + chr(114) + chr(1)

try:
    tn = telnetlib.Telnet("192.168.31.87", 9100, 3)
except:
    print 'Error connect'
    sys.exit(0)
tn.write(fil1nam + '\n' +
          fil1cont + '\n' * 7 + cutprn)  # делаем запрос

print 'Upload to printer'

time.sleep(2)
tn.write(tstatus)
rstatus = tn.read_all()
print str(rstatus)
tn.close()
