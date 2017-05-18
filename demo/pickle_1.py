#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle

d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

f = open('dumps.txt', 'wb')
pickle.dump(d, f)
f.close()

print('\033[32m****************************\033[0m')
f = open('dumps.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)