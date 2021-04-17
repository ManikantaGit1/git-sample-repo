import pytest
from utilities.cutom_logger import CustomLogger as cl
from selenium import webdriver
from pages.home.login_page import LoginPage
from base.Webdriverfactory import WebDriverFactory
log=cl()
@pytest.fixture()
def setUp(request):
    log.info('Run before every test')
    yield
    log.info('\nRun after every test')


@pytest.fixture(scope='class')
def OneTimesetUp(request,browser,osType):
    log.info('Run Once before all the test')
    wdf=WebDriverFactory(browser)
    driver=wdf.getWebDriver()
    lp = LoginPage(driver)
    lp.getLoginDetails(username='standard_user', password='secret_sauce')
    if osType=='windows':
        log.info("Running tests on WindowsOs")
    else:
        log.info("Running tests on MacOs")
    if request.cls is not None:
        request.cls.driver=driver

    yield driver
    driver.quit()
    log.info('\nRun Once after all the test')

def pytest_addoption(parser):
    parser.addoption('--browser',help="This is for Browser")
    parser.addoption('--osType',help="This is the Os type")


@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')

@pytest.fixture(scope='session')
def osType(request):
    return request.config.getoption('--osType')

