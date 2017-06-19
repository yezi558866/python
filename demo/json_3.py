#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

def load():
	with open('data.json', 'r') as json_file:
		data = json.load(json_file)
		return data

ddata = load()
print(ddata)
print(type(ddata))

print(type(ddata['Openfile']))
print(type(ddata['Openfile'][0]))
print(ddata['Openfile'][0])
print(ddata['Openfile'][1])