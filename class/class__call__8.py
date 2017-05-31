#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Student(object):
	def __init__(self, name):
		self.name = name

	def __call__(self):
		print('My name is %s.' % self.name)

s = Student('Michael')
print(s)
print('\33[32m***********************\33[0m')
print(s())
print('\33[32m***********************\33[0m')
s()

print('\33[32m***********************\33[0m')
print(callable(Student('Michael')))
print('\33[32m***********************\33[0m')
print(callable(max))
print('\33[32m***********************\33[0m')
print(callable([1, 2, 3]))
print('\33[32m***********************\33[0m')
print(callable(None))
print('\33[32m***********************\33[0m')
print(callable('str'))