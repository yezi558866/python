#!/usr/bin/python
#Flename: fun2.py

def sayhi():
	name = raw_input('Enter your name: ')
	print '\33[32mHello %s, welcome to wuhan! \33[0m' %name

	if name == 'bobo':
		print '\33[36m%s is a awesome boy!\33[0m' %name
	else:
		print 'Our`s work is IT!'
sayhi()
