#!/usr/bin/python3
# -*- coding: utf-8 -*-

from parameterized import parameterized, param
import unittest
import json

def load():
	with open('test_menu.json', 'r') as json_file:
		data = json.load(json_file)
		return data

ddata = load()
params = ddata['OpenFile']

print('***********************************')
print(params)
print(type(params))
print(params[0])
print(type(params[0]))
print('***********************************')
#print(tuple(params[0].values()))

def load_test_cases(params):
	params_tuple = []
	for each in params:
		#print(each)
		params_tuple.append(tuple(each.values()))
	return params_tuple

aa = load_test_cases(params)
print(aa)