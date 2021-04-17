from selenium import webdriver
import os
from traceback import print_stack
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import time
import inspect,random
from utilities.cutom_logger import CustomLogger as cl
import logging


class SeleniumDriver():
    log = cl(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getText(self,ele):
        return ele.text

    def getByTypes(self, locatorType):
        if locatorType == 'id':
            return By.ID
        if locatorType == 'xpath':
            return By.XPATH
        if locatorType == 'name':
            return By.NAME
        if locatorType == 'link':
            return By.LINK_TEXT
        if locatorType == 'css':
            return By.CSS_SELECTOR
        if locatorType == 'class':
            return By.CLASS_NAME
        else:
            return By.locatorType

    def getElement(self,locator,locatorType='id'):
        try:
            if self.IsElementPresent(locator, locatorType=locatorType) == True:
                locatorByType = self.getByTypes(locatorType)
                return self.driver.find_element(locatorByType, locator)
                self.log.info("Element Present")
            else:
                return None
        except Exception as e:
            self.log.info("Element not found" + "\nMethod Name::" + str(inspect.stack()[0][3]) + "\nClass Name::" + str(
                self.__class__) + str(e))
            print_stack()

    def getElementList(self,locator,locatorType='id'):
        try:
            if self.IsElementPresent(locator, locatorType=locatorType) == True:
                locatorByType = self.getByTypes(locatorType)
                return self.driver.find_elements(locatorByType, locator)
                self.log.info("Element List present")
            else:
                return None
        except Exception as e:
            self.log.info("Element List not found" + "\nMethod Name::" + str(inspect.stack()[0][3]) + "\nClass Name::" + str(
                self.__class__) + str(e))
            print_stack()

    def ElementClick(self, locator='', locatorType='id',element=''):
        try:
            if locator:
                element = self.getElement(locator,locatorType=locatorType)
            element.click()
            self.TakeScreenShot()
            self.log.info("Element Clicked", inspect.stack()[0][3])
        except Exception as e:
            self.log.info(
                "\nMethod Name::" + str(inspect.stack()[0][3]) + "\nClass Name::" + str(self.__class__) + str(e))
            print_stack()


    def SendKeys(self, locator='', val='', locatorType='id',element=''):
        try:
            if locator:
                element=self.getElement(locator,locatorType=locatorType)
            element.send_keys(val)
            self.log.info("Values passed to the field" + inspect.stack()[0][3])
        except Exception as e:
            self.log.info(
                "\nMethod Name::" + str(inspect.stack()[0][3]) + "\nClass Name::" + str(self.__class__) + str(e))
            print_stack()

    def IsElementPresent(self, locator, locatorType="id"):
        try:
            element = self.driver.find_element(locatorType, locator)
            if element is not None:
                self.log.info("element found " + inspect.stack()[0][3])
                return True
            else:
                self.log.info("element Not found")
                return False
        except Exception as e:
            return False
            self.log.info(
                "\nMethod Name::" + str(inspect.stack()[0][3]) + "\nClass Name::" + str(self.__class__) + str(e))
            print_stack()

    def TakeScreenShot(self):
        try:
            error = self.IsElementPresent("//div[@class='error-message-container error']/h3", locatorType='xpath')
            if error:
                filename = '/Users/manikantauttarkar/PycharmProjects/workspace/automation_framework/screenshots/{0}.png'.format(random.random())
                # filename = '/Users/manikantauttarkar/PycharmProjects/workspace/automation_framework/screenshots/test.png'
                self.driver.save_screenshot(filename)
                self.log.info("FAILURE!! and \n screenshot saved in path::" + filename)
            else:
                self.log.info(
                    "No ScreenShot Taken!! No Errors")

        except Exception as e:
            self.log.info("No ScreenShot Taken!! No Errors")
            print_stack()

    def waitClick(self, locator, locatorType='id'):
        try:
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException, ElementClickInterceptedException,
                                                     StaleElementReferenceException])
            w = wait.until(EC.element_to_be_clickable((self.getByTypes(locatorType),locator)))
            w.click()
            self.TakeScreenShot()
            self.log.info("waitclick button was sucessfully clicked")
        except Exception as e:
            self.log.info("exception Wait function in Selenium Driver Class" + str(e))
            print_stack()

    def waitVisible(self, locator, locatorType='id'):
        try:
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException, ElementClickInterceptedException,
                                                     StaleElementReferenceException])
            w = wait.until(EC.presence_of_element_located((self.getByTypes(locatorType),locator)))
            w.click()
            self.TakeScreenShot()
            self.log.info("waitVisible Button successfully clicked")
        except Exception as e:
            self.log.info(e)
            print_stack()