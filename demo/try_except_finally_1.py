#!/usr/bin/env python3
# -*- coding: utf-8 -*_

class AError(Exception):
	"""AError---exception"""
	print('AError')

try:
	#raise AError
	$asdas('123')
	#abs(123)
except AError:
	print("Get AError")
except:
	print("except")
else:
	print("else")
finally:
	print("finally")
print("hello world")