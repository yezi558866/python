#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#对list进行排序
a = sorted([36, 5, -12, 9, -21])
print(a)
print('\033[32m****************************\033[0m')

#可以接受一个k函数实现自定义排序，如按绝对值大小排序：
b = sorted([36, 5, -12, 9, -21], key=abs)
print(b)
print('\033[32m****************************\033[0m')

#字符串排序，按照ASCII的大小排序。由于‘Z’ < 'a'
c = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(c)
print('\033[32m****************************\033[0m')

#忽略大小写排序:
d = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(d)
print('\033[32m****************************\033[0m')

#忽略大小写且反向排序:
e = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(e)
print('\033[32m****************************\033[0m')