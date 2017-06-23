#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest

class Loader(unittest.TestLoader):  
    def getTestCaseNames(self, testCaseClass):  
        """Return a sorted sequence of method names found within testCaseClass 
        """  
        testFnNames = unittest.TestLoader.getTestCaseNames(self, testCaseClass)  
  
        def isParameterizedMethod(attrname, testCaseClass=testCaseClass,  
                         prefix="parameterized"):  
            return attrname.startswith(prefix) and hasattr(getattr(testCaseClass, attrname), '__call__')  
  
        testFnNames0 = filter(isParameterizedMethod, dir(testCaseClass))  
        for func in testFnNames0:  
            name = func.split("_", 1)[1]  
            collect = "collection_" + name  
            if hasattr(getattr(testCaseClass, collect), '__call__'):  
                collectFunc = getattr(testCaseClass, collect)  
                for item in range(len(collectFunc())):  
                    testFnNames.append("%s_%d" % (name, item))  
  
        if self.sortTestMethodsUsing:  
            testFnNames.sort(key=_CmpToKey(self.sortTestMethodsUsing))  
        return testFnNames  