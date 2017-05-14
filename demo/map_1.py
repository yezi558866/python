#!/usr/bin/env python3
# -*- coding: utf-8 -*_

#from functools import reduce

def f(x):
	return x*x

r = map(f, [1, 2])
b = map(f, range(1,6))
c = map(lambda x:x*x*x, range(1,6))
print(list(r))
print(list(b))
print(list(c))