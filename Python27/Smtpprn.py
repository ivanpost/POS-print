#!/usr/bin/python2
# -*- coding: utf-8 -*-
import os
import telnetlib
import sys
import shutil

import smtplib

text = 'usus Order number 00000041\n\n Hello from Python'
onump = text.find('Order number')

if onump > 0:
    sbjkt = 'Ord: ' + text[onump + 13 : onump + 22]
else:
    sbjkt = 'Temp'

HOST = 'smtp.gmail.com'
FROM = 'rest.goodkarma@gmail.com' 
TO = ['x1076@yandex.ru'] + ['ivanpost@mail.ru']
MESSAGE = 'Subject: ' + sbjkt + '\n\n' + text

smtpObj = smtplib.SMTP(HOST, 587)
smtpObj.starttls()
smtpObj.login(FROM,'Rg**2')

smtpObj.sendmail(FROM, TO, MESSAGE)
smtpObj.quit()
