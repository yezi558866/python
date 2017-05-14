#!/usr/bin/env python3
# -*- coding: utf-8 -*_

from inspect import isgeneratorfunction
from collections import Iterable

def fab(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a+b
		n = n + 1

for n in fab(6):
	print(n)
print('\033[32m****************************\033[0m')
f = fab(6)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print('\033[32m****************************\033[0m')
#fab是一个generator function, fab(5)是调用fab返回的一个generator。好比类的定义和类的实例。
print(isgeneratorfunction(fab))  
print(isgeneratorfunction(fab(5)))
print('\033[32m****************************\033[0m')
print(isinstance(fab, Iterable))
print(isinstance(fab(5), Iterable))

'''
0, 0, 1
1, 1, 1
2, 1, 2
3, 2, 3
4, 3, 5
5, 5, 8
'''