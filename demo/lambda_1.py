#!/usr/bin/env python3
# -*- coding: utf-8 -*_

from functools import reduce

g = lambda x,y:x+y
a = g(2,3)
print(a,'\n')

l = range(1, 6)
f = lambda x,y : x*y
print(reduce(f, l))