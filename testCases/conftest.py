import os.path
from datetime import datetime

import pytest
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def setup(browser):

    if browser == "edge":
        from selenium.webdriver.edge.service import Service
        ops = webdriver.EdgeOptions()
        service = Service(executable_path=EdgeChromiumDriverManager().install())
        driver = webdriver.ChromiumEdge(service=service,options=ops)
        yield driver
        driver.close()

    if browser == "firefox":
        from selenium.webdriver.firefox.service import Service
        ops = webdriver.FirefoxOptions()
        service=Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service,options=ops)
        yield driver
        driver.quit()

    if browser == "chrome":
        from selenium.webdriver.chrome.service import Service
        ops = webdriver.ChromeOptions()
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service,options=ops)
        yield driver
        driver.close()

    if browser == "opera":
        from selenium.webdriver.chrome.service import Service
        ops = webdriver.ChromeOptions()
        service = Service(executable_path=r'C:\Drivers\operadriver_win64\operadriver_win64\operadriver.exe')
        driver = webdriver.remote(service=service,options=ops)
        yield driver
        driver.close()



def pytest_addoption(parser):
    # Add a custom command-line option to specify the browser
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome, firefox, etc.")

@pytest.fixture()
def browser(request):
    # Get the value of the custom option --browser
    return request.config.getoption("--browser")



########################### HTML ##################################


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath=os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"