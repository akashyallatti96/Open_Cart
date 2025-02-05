import os.path
import time

from pageObjects.HomePage import HomePage
from pageObjects.RegisterAccout import RegisterAccount
from utilities.randomString import randon_string_generator
from utilities.readProperties import ReadConfig
from utilities.cutsomLogger import LogGen

class TestRegisterFunctionalityTC001():
    baseURL = ReadConfig.get_app_url()


    def test_account_reg(self,setup):
        self.driver = setup
        self.driver.get(url=self.baseURL)
        self.logger = LogGen.loggen()
        self.logger.debug("OPened")
        self.logger.critical("Opened application")
        time.sleep(2)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


        # self.hp = HomePage(self.driver)
        self.reg = RegisterAccount(driver=self.driver)
        # self.hp.click_my_account()
        # self.hp.click_register()

        self.reg.set_first_name("Akash0")
        self.reg.set_last_name("Yall0")
        self.email = randon_string_generator(size=10) + "@gmail.com"
        self.reg.set_email(self.email)
        self.reg.set_password("abcdefg")
        self.reg.subscribe_newsletter()
        self.reg.accept_policy()
        time.sleep(5)
        self.reg.click_continue()
        actual_message = self.reg.get_confirmation_message()
        excepted_message ="Your Account Has Been Created!"
        if actual_message == excepted_message:
            print(self.email)
            assert True
        else:
            self.driver.save_screenshot(os.path.curdir+"\\screenshots\\TestRegisterFunctionalityTC001.png")
            assert False
