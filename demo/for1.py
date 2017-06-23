#!/usr/bin/python
#Filename: for1.py

import subprocess, os

aa_list = ['true', 'false']
b = aa_list[1]
print(b)
print('\33[32m***********************\33[0m')
s = 'ab,cde,fgh,ijk'
print(s.split(','))

print('\33[32m***********************\33[0m')
for i in range(1, 15):
	print(i)
else:
	print('The loop is down!')

print('\33[32m***********************\33[0m')

def fun(fi, li): 
	for ii in li:
		if ii == fi:
			return 1
	else:
		print('No!!')

fi = 'cc'
li = ['aa', 'bb', 'cc']

print(fun(fi, li))

print('\33[32m***********************\33[0m')

class A(object):
	def foo(self, x):
		print("executing foo(%s, %s)" % (self, x))

	@classmethod
	def class_foo(cls, x):
		print("executing class_foo(%s, %s)" % (cls, x))

	@staticmethod
	def static_foo(x):
		print("executing static_foo(%s)" % x)

a = A()

a.foo(1)
print('\33[32m***********************\33[0m')
a.class_foo(1)
print('\33[32m***********************\33[0m')
a.static_foo(1)
print('\33[32m***********************\33[0m')
a.static_foo('hi')
print('\33[32m***********************\33[0m')
