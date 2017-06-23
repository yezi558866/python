#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest

class Test(unittest.TestCase):  
  
    def __init__(self, methodName='runTest'):  
        def isParameterizedMethod(attrname):  
            return attrname.startswith("parameterized") and hasattr(getattr(self, attrname), '__call__')  
  
        testFnNames = filter(isParameterizedMethod, dir(self))  
        for func in testFnNames:  
            name = func.split("_", 1)[1]  
            collect = "collection_" + name  
            if hasattr(getattr(self, collect), '__call__'):  
                collectFunc = getattr(self, collect)  
                array = collectFunc()  
                for index in range(len(array)):  
                    test = "%s_%d" % (name, index)  
                    setattr(self.__class__, test, getattr(self, func)(array[index]))  
  
        # must called at last  
        unittest.TestCase.__init__(self, methodName)