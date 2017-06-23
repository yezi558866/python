#!/usr/bin/python3
# -*- coding: utf-8 -*-

from nose.tools import assert_equal
from parameterized import parameterized, param

import unittest
import math

@parameterized([
	(2, 2, 4),
	(2, 3, 8),
	(1, 9, 1),
	(0, 9, 0),
])

def test_pow(base, exponent, expected):
	assert_equal(math.pow(base, exponent), expected)

class TestMathUnitTest(unittest.TestCase):
	@parameterized.expand([
		("negative", -1.5, -2.0),
		("integer", 1, 1.0),
		("large fraction", 1.6, 1),
	])

	def test_floor(self, name, input, expected):
		assert_equal(math.floor(input), expected)

class Test_list_of_tuples(unittest.TestCase):
	@parameterized.expand([
		(2, 3, 5),
		(3, 5, 8),
	])

	def test_add(self, a, b, expected):
		assert_equal(a + b, expected)

class Test_list_of_params(unittest.TestCase):
	@parameterized.expand([
		param("10", 10),
		param("10", 16, base=16),
	])

	def test_int(self, str_val, expected, base=10):
		assert_equal(int(str_val, base=base), expected)
'''
class Test_iterable_of_params(unittest.TestCase):
	@parameterized.expand(
		param.explicit(*json.load(line))
		for line in open("testcases.jsons")
	)

	def test_from_json_file(self, ...):
		...
'''
class Test_callable_list_of_tuples(unittest.TestCase):
	def load_test_cases():
		return [
			("test", ),
			("test", ),
		]

	@parameterized.expand(load_test_cases)

	def test_from_function(self, name):
		assert_equal(name, "test")