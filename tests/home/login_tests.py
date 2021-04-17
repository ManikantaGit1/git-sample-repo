from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import time
import inspect
import pytest
import logging
import unittest
from utilities.cutom_logger import CustomLogger as cl

@pytest.mark.usefixtures('OneTimesetUp','setUp')
class LoginTests(unittest.TestCase):
    log=cl()

    @pytest.fixture(autouse=True)
    def objectsetup(self,OneTimesetUp):
        self.lp = LoginPage(self.driver)

    def test_validLogin(self):
        self.lp.getLoginDetails(username='standard_user', password='secret_sauce')
        result = self.lp.VerifyLoginSuccess()
        assert result == True
        self.log.info("Login Successfull")

    def test_InvalidLogin(self):
        self.lp.LogOut()
        self.lp.getLoginDetails(username="", password="")
        result = self.lp.InvalidLogin()
        assert result == True
        self.log.info("Login Failed")



# t=TestFramework()
# t.test_validLogin()
# t.test_InvalidLogin()
