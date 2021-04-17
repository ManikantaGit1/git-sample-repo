from base.base_class import BaseClass
import time
from utilities.cutom_logger import CustomLogger as cl
from pages.home.login_page import LoginPage
import pytest

# Locators for details in CheckoutPage MethodName: EnterDetails()
_firstName = "first-name"
_lastName = "last-name"
_zipCode = "postal-code"



@pytest.mark.usefixtures('ProductDriver')
class PurchaseProduct(BaseClass):
    log = cl()

    def __init__(self, driver):
        super().__init__(driver)
        self.lp = LoginPage(self.driver)

    def AddItem(self, locator, locatorType='id'):
        ele = self.getElement(locator, locatorType=locatorType)
        if ele is not None:
            self.waitVisible(locator, locatorType=locatorType)
            self.log.info("Item Added to the Cart")
        else:
            self.log.info("Element is not present or is returning None")

    def AddItems(self,locator, locatorType='id'):
        ele = self.getElementList(locator, locatorType=locatorType)
        for i in ele:
            # e=i.get_attribute('id')
            self.ElementClick(element=i)
        self.log.info("all the items added to the Cart")
        # if ele is not None:
        #     time.sleep(2)
        #     print(ele)
        #     self.waitVisible(locator, locatorType=locatorType)
        #     self.log.info("Item Added to the Cart")
        # else:
        #     self.log.info("Element is not present or is returning None")

    def NumberOfCartItems(self, locator, locatorType='id'):
        it = self.getElement(locator, locatorType=locatorType)
        if it is not None:
            self.log.info("The Number of Items in The Kart are :: " + it.text)
            # self.waitVisible(locator, locatorType=locatorType)
            # self.log.info("The Kart Icon Clicked")
        else:
            self.log.info("NoItems added to the Kart")

    def ItemPresentInKart(self, locator, locatorType='id'):
        lis=[]
        it = self.getElementList(locator, locatorType=locatorType)
        for i in it:
            if i is not None:
                self.log.info("Items present in Kart is :: " + i.text)
                lis.append(i.text)
            else:
                self.log.info("No item is present in the Kart")

        return lis


    def EnterDetails(self, firstname='', lastname='', zipcode=''):
        fn = self.lp.getElement(_firstName)
        self.lp.SendKeys(element=fn, val=firstname)
        ln = self.lp.getElement(_lastName)
        self.lp.SendKeys(element=ln, val=lastname)
        pc = self.lp.getElement(_zipCode)
        self.lp.SendKeys(element=pc, val=zipcode)

    def NavigateToAllItems(self):
        self.lp.getElement('react-burger-menu-btn').click()
        time.sleep(2)
        self.lp.getElement('inventory_sidebar_link').click()

