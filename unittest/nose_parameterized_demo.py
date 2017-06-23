#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from parameterized import parameterized

class TestMathUnitTest(unittest.TestCase):

	@classmethod
	def setUp(cls):
		pass

	params = [
		("1st", 4, 5),
		("2en", 2, 3),
		("3rd", 3, 4),	
	]

	@parameterized.expand(input = params)
	def test_floor(self, name, source, expected):
		self.assertEqual(source + 1, expected)

if __name__ == '__main__':
	unittest.main()