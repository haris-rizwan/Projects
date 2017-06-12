import unittest
from unitTestPackage.UnitTestExample import TestingPackageExample
from unitTestPackage.UnitTestExampl2 import TestingExamplePackage2

#1st step get all the test cases from the files that you want to run
TC1 = unittest.TestLoader().loadTestsFromTestCase(TestingPackageExample)
TC2 = unittest.TestLoader().loadTestsFromTestCase(TestingExamplePackage2)

#2nd step Now we have create a test suite

First_suite = unittest.TestSuite([TC1,TC2])

unittest.TextTestRunner(verbosity=2).run(First_suite)


