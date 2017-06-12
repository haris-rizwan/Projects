import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import unittest
from selenium.webdriver import ActionChains
import os
import time

@pytest.fixture()
def setUp():
    print("Running demo 1 setup")
    yield   # everything after the yeild will be executed after the every method
    # you do not have to write a different method for tear down .
    print("Running demo 1 teardown")

def test_demo1_methodA(setUp):
    print("running method A")

def test_demo1_methodB(setUp):
    print("running method b")