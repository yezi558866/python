#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print(os.name)  #操作系统类型
print('\033[32m****************************\033[0m')
print(os.uname)  #获取详细的系统信息
print('\033[32m****************************\033[0m')
#print(os.environ)  #操作系统中定义的环境变量
print('\033[32m****************************\033[0m')
print(os.environ.get('PATH'))
print('\033[32m****************************\033[0m')
print(os.path.abspath('.'))
print('\033[32m****************************\033[0m')
print(os.path.join('/home/pro/python/os', 'testdir'))
print('\033[32m****************************\033[0m')
os.mkdir('/home/pro/python/os/testdir')
print('\033[32m****************************\033[0m')
os.rmdir('/home/pro/python/os/testdir')

print('\033[32m****************************\033[0m')
print(os.path.split('/home/pro/python/os/testdir/tile.txt'))

print('\033[32m****************************\033[0m')
print(os.path.splitext('/home/pro/python/os/testdir/tile.txt'))

print('\033[32m****************************\033[0m')
#os.rename('test.txt', 'test.py')

print('\033[32m****************************\033[0m')
#os.remove('test.py')

print('\033[32m****************************\033[0m')
print([x for x in os.listdir('.') if os.path.isdir(x)])

print('\033[32m****************************\033[0m')
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])