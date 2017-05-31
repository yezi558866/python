#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Student(object):

	def get_score(self):
		return self._score

	def set_score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value

class Student(object):

	@property
	def score(self):
		return self._score

	@score.setter:
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value

#birth是可读写属性，age是一个只读属性。
class Student(object):

	@property
	def birth(self):
		return self._birth
	
	@birth.setter
	def birth(self, value):
		self._birth = value

	@property
	def age(self):
		return 2015 - self._birth