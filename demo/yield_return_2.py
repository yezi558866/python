#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def read_file(fpath):
	BLOCK_SIZE = 1024
	with open(fpath, 'rb') as f:
		while True:
			block = f.read(BLOCK_SIZE)
			if block:
				yield block
			else:
				return

f = read_file('/home/pro/python/demo/yield_return_2.py')
for i in range(1,17):
	print(next(f))
	#print('\n')