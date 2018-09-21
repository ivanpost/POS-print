#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os
import telnetlib
import sys
import shutil


directory = '/home/pi/Python2'
mdirectory = '/home/pi/Python2/Tmp'
files = os.listdir(directory)
txtf = filter(lambda x: x.endswith('.txt'), files) 
pfilnam = open(txtf[0])
pfiltxt = pfilnam.read()
myfilen.close()
pfilnam = str
#shutil.move(directory + 

cutprn = chr(27) + chr(105)
upsdwn = chr(27) + chr (123) + chr (1)
upsup = chr(27) + chr (123) + chr (0)
try:
    tn = telnetlib.Telnet("192.168.31.87", 9100, 3)
except:
    print 'Error connect'
    sys.exit(0)
tn.write('1 zapr vsep 2 zapr vsep 3 zapr vsep 4 zapr vsep\n' * 3 +
          str(txtf) + str(myfilen) + '\n' +
          myfilet +
          '\n' * 2 + upsdwn + 'ASDFG ' * 3 + 
          '\n' * 5 + upsup + cutprn)  # делаем запрос

tn.close()
print 'Telnet OK'

