from base.selenium_driver import SeleniumDriver
import random
import string
from string import ascii_letters


class BaseClass(SeleniumDriver):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    def ScrollPage(self,direction='up'):
        try:
            if direction=='up':
                self.driver.execute_script('window.scrollBy(0,-1000);')
                self.log.info("Scrolled up")
            elif direction=='down':
                self.driver.execute_script('window.scrollBy(0,1000);')
                self.log.info("Scrolled down")
        except Exception as e:
            self.log.error("Error encountered while scrolling"+str(e))


    def RandomAlfaNumeric(self,length=10,characterType='upper'):
        if characterType=='upper':
            return string.ascii_letters.upper()[:length]
        elif characterType=='lower':
            return string.ascii_letters.lower()[:length]
        elif characterType=='digit':
            return int(str(random.randrange(23241323*1000,22020020*10000))[:length])
        elif characterType=='mix':
            return (str(random.randrange(100, 10000)) + string.ascii_letters.lower())[:length]
        else:
            return random.choice(ascii_letters)*[length]






