#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
from io import BytesIO

#把str写入StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

print('\033[32m****************************\033[0m')
#读取StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())

print('\033[32m****************************\033[0m')
#写入BytesIO：
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
print(f.getvalue().decode('utf-8'))



print('\033[32m****************************\033[0m')
#读出BytesIO:
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
print(f.read().decode('utf-8'))

print('\033[32m****************************\033[0m')
#seek、tell改变stream position介绍。
f = StringIO()
print(f.tell())
f.write('Hello World')
print(f.tell())
print(f.seek(0)) 
s = f.readline()
print(s)