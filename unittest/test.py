#!/usr/bin/python3
# -*- coding: utf-8 -*-

from unittest import *  
from Test import *  
from Loader import *  
  
class TestFunctions(Test):  
    @classmethod  
    def collection_test_add(cls):  
        return [1,2,3,5,7,9]  
  
    def parameterized_test_add(self, x):  
        def test_body(self):  
            print(x * x)  
        return test_body  
  
if __name__ == '__main__':  
    suite = Loader().loadTestsFromTestCase(TestFunctions)  
    runner = unittest.TextTestRunner()  
    rc = runner.run(suite)  
    print(rc)