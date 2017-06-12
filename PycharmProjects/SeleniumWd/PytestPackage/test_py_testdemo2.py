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
    print("Running demo 2 setup")
    yield
    print("Running demo 2 teardown")

def test_demo2_methodA(setUp):
    print("running method A")

def test_demo2_methodB(setUp):
    print("running method b")