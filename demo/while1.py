#!/usr/bin/python
#Filename:while1.py

b=20

running = True
print '\033[32m*****************************\033[0m'
while running:
	a = int(raw_input('Enter a number:'))
	if a == b:
		print '\033[32mGood, a=%s is equal b=%s !\033[0m' %(a, b)
		running = False
	elif a < b:
		print '\033[32mNo, a is little than b.\033[0m'
	else:
		print '\033[32mNo, a is greater than b.\033[0m'
else:
	print 'The loop is down!'
