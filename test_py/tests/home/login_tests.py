from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.lp = LoginPage(self.driver)
    @pytest.mark.run(order=1)
    def test_invalidlogin(self):
        result=self.lp.login()
        return result

