#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
	f = open('open_file_1.py','r')
	print(f.read())
finally:
	if f:
		f.close()

print('\033[32m****************************\033[0m')

with open('open_file_1.py', 'r') as f:
	print(f.read())

print('\033[32m****************************\033[0m')

f = open('open_file_1.py','r')
for line in f.readlines():
	print(line.strip()) #把末尾的'\n'删掉