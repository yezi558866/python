#!/usr/bin/python
#Filename: break1.py

while True:
	A = raw_input('Enter a number: ')
	if A == '23':
		print 'The number is %s !' %A
		break
	else:
		print 'Please continue enter number.'
print 'Down! You guess right!'
