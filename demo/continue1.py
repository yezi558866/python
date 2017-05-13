#!/usr/bin/python
#Filename : continue1.py

while True:
	A = int(raw_input('Enter a number : '))
	if A == 23:
		print 'The number is %s !' %A
		break
	if A  > 20:
		continue
	print 'Please continue enter number.'

print 'Down!'
