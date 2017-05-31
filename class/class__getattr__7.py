#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Student(object):

	def __init__(self):
		self.name = 'Michael'

	def __getattr__(self, attr):
		if attr == 'score':
			return 99
		elif attr == 'age':
			return lambda: 25
		raise AttributeError('\'Student\' object has no attribute \'%s\'' %attr)


s = Student()
print(s.name)
print(s.score)

print(s.age)
print(s.age())
print(s.aa)