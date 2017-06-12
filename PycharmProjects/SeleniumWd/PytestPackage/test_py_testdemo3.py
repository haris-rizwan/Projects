import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import unittest
from selenium.webdriver import ActionChains
import os
import time

#
# file name chould start with test
# test method name should start with test
#
#
# py.test test_mod.py #runs test in module
# py.test. sampath # run all test below same path
# py.test test_module.py::test_method # only run the test_method in test_module
#

@pytest.fixture()
def setUp():
    print("Running demo 3 setup")
    yield
    print("Running demo 3 teardown")

def test_demo3_methodA(setUp):
    print("running method A")

def test_demo3_methodB(setUp):
    print("running method b")