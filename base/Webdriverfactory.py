from selenium import webdriver


class WebDriverFactory():

    def __init__(self,browser):
        self.browser=browser

    def getWebDriver(self):
        if self.browser=='chrome':
            driver=webdriver.Chrome()
        elif self.browser=='firefox':
            driver=webdriver.Firefox()
        else:
            driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        BaseUrl = "https://www.saucedemo.com"
        driver.get(BaseUrl)
        return driver