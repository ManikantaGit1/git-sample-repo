from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import random
import inspect
from traceback import print_stack
import time
from base.selenium_driver import SeleniumDriver


# @pytest.mark.usefixtures('OneTimesetUp','setUp')
class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _username = "user-name"
    _password = "password"
    _loginButton = "login-button"

    def getUsername(self, username):
        self.SendKeys(self._username, val=username, locatorType='id')

    def getPassword(self, password):
        self.SendKeys(locator=self._password, val=password, locatorType='id')

    def clickLogin(self):
        self.waitClick(locator=self._loginButton, locatorType='id')
        try:
            self.TakeScreenShot()
        except:
            self.log.info("The Login button Successfully Clicked,No Screenshot taken in" + "Method Name::" + str(
                inspect.stack()[0][3]))

    def getLoginDetails(self, username, password):
        self.getUsername(username)
        self.getPassword(password)
        self.clickLogin()
        # time.sleep(2)
        # self.driver.execute_script('window.scrollBy(0,1000);')
        # time.sleep(2)
        # self.driver.execute_script('window.scrollBy(0,-1000);')
        # time.sleep(2)

    def VerifyLoginSuccess(self):
        result = self.IsElementPresent("//a[@id='item_4_title_link']", locatorType='xpath')
        return result

    def InvalidLogin(self):
        result = self.IsElementPresent("//div[@class='error-message-container error']/h3", locatorType='xpath')
        return result

    def LogOut(self):
        """

        :rtype: object
        """
        self.ElementClick('react-burger-menu-btn')
        self.ElementClick('logout_sidebar_link')
