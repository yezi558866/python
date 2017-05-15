#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
from io import BytesIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

print('\033[32m****************************\033[0m')

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())

print('\033[32m****************************\033[0m')
'''
f = BytesIO()
f.write('中文', encode('utf-8'))
print(f.getvalue())
'''


print('\033[32m****************************\033[0m')
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())