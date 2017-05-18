#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))
print(type(json.dumps(d)))  #str类型

print('\033[32m****************************\033[0m')
json_str = '{"age": 20, "name": "Bob", "score": 88}'
print(json.loads(json_str))
print(type(json.loads(json_str)))

print('\033[32m****************************\033[0m')
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
	return{
		'name': std.name,
		'age': std.age,
		'score': std.score
	}

s = Student('Bob', 20, 88)
print(type(s))  #类实例，不能被json化，必须先转化为字典
print(json.dumps(s, default=student2dict))

print('\033[32m****************************\033[0m')
print(json.dumps(s, default=lambda obj: obj.__dict__))

print('\033[32m****************************\033[0m')
def dict2student(d):
	return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))