#!/usr/bin/python3
# -*- coding: utf-8 -*-

from types import MethodType

class Student(object):
	pass

s = Student()
s.name = 'Michael'
print(s.name)

#给实例绑定方法：
def set_age(self, age):
	self.age = age

s.set_age = MethodType(set_age, s)
s.set_age(25)
s.age

#给class绑定方法：
def set_score(self, score):
	self.score = score
Student.set_score = set_score

#使用__slots__限制实例的属性。
clsaa Student(object):
	__slots__ = ('name', 'age') #用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Michael'
s.age = 25
s.score = 99

#子类不受__slots__的限制。
class GraduateStudent(student):
	pass

g = GraduateStudent()
g.score = 9999