#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os
import telnetlib
import sys

cutprn = chr(27) + chr(105)
upsdwn = chr(27) + chr (123) + chr (1)
upsup = chr(27) + chr (123) + chr (0)
try:
    tn = telnetlib.Telnet("192.168.31.87", 9100, 3)
except:
    print 'Error telnet'
    sys.exit(0)
tn.write('1 zapr vsep 2 zapr vsep 3 zapr vsep 4 zapr vsep\n' * 10 +
         '\n' * 2 + upsdwn + 'ASDFG ' * 3 + 
		 '\n' * 5 + upsup + cutprn)  # делаем запрос

tn.close()
print 'Telnet OK'
tn.close()
