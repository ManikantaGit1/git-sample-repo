from pages.products.purchase_products import PurchaseProduct
from tests.home.login_tests import LoginPage
import unittest, pytest, time, inspect
from utilities.cutom_logger import CustomLogger as cl
from ddt import ddt, data, unpack
from utilities.read_data import getCsvData

# locators
_addItemButton = "//button[@id='add-to-cart-sauce-labs-backpack']"
_NumberOfKartItmes = "//span[@class='shopping_cart_badge']"
_itemName = "//a[@id='item_4_title_link']/div"
_KartIcon = "//*[@id='shopping_cart_container']/a"
_CheckOut = "checkout"
_Continue = 'continue'
_Finish = 'finish'
_BackHome = 'back-to-products'
_ProductList = "//div[@class='inventory_item_label']/a/div"
_cartItemList = "//div[@class='cart_item_label']/a/div"
_addButtons = "//div[@class='pricebar']//button"


@ddt()
@pytest.mark.usefixtures('OneTimesetUp', 'setUp')
class TestOrderProduct(unittest.TestCase):
    log = cl()

    @pytest.fixture(autouse=True)
    def classSetup(self, OneTimesetUp):
        self.lp = LoginPage(self.driver)
        self.pp = PurchaseProduct(self.driver)

    # def setUp(self) -> None:
    #     self.pp.NavigateToAllItems()

    @data(*getCsvData('/Users/manikantauttarkar/PycharmProjects/workspace/automation_framework/testdata.csv'))
    @unpack
    def test_purchase(self, firtsName, lastName, zipCode):
        self.pp.AddItem(_addItemButton, locatorType='xpath')
        # self.pp.AddItems(_addButtons, locatorType='xpath')
        self.pp.NumberOfCartItems(_NumberOfKartItmes, locatorType='xpath')
        actualText = self.pp.ItemPresentInKart(_itemName, locatorType='xpath')
        self.pp.ScrollPage(direction='up')
        self.lp.waitVisible(locator=_KartIcon, locatorType='xpath')
        # self.pp.ScrollPage(direction='down')
        # exceptedText = self.pp.ItemPresentInKart(_cartItemList, locatorType='xpath')
        # assert len(actualText) == len(exceptedText)
        # self.log.info("Item" + str(actualText) + "added successfully to Kart and Verified")
        # self.pp.ScrollPage(direction='down')
        self.lp.waitClick(_CheckOut)
        self.pp.EnterDetails(firstname=firtsName, lastname=lastName, zipcode=zipCode)
        self.lp.waitClick(locator=_Continue)
        self.pp.ScrollPage(direction='down')
        self.lp.waitClick(locator=_Finish)
        self.pp.ScrollPage(direction='up')
        self.lp.waitClick(locator=_BackHome)
