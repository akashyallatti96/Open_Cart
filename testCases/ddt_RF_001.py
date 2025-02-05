import os.path
import time

from pageObjects.HomePage import HomePage
from pageObjects.RegisterAccout import RegisterAccount
from utilities.randomString import randon_string_generator
from utilities.readProperties import ReadConfig
from utilities.cutsomLogger import LogGen
from utilities import xlUtiles

class TestRegisterFunctionalityTC001():
    baseURL = ReadConfig.get_app_url()


    def test_account_reg(self,setup):
        self.driver = setup
        self.logger = LogGen.loggen()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


        # self.hp = HomePage(self.driver)

        # self.hp.click_my_account()
        # self.hp.click_register()

        file = 'E:\\Selenium_Project\\Open_Cart\\testData\\Data.xlsx'
        sheetName = "Register"
        rows = xlUtiles.get_row_count(file,sheetName)
        columns = xlUtiles.get_column_count(file,sheetName)
        self.driver.get(url=self.baseURL)
        for r in range(2,rows):

            time.sleep(2)
            self.reg = RegisterAccount(driver=self.driver)
            first_name = xlUtiles.read_data(file,sheetName,r,1)
            last_name = xlUtiles.read_data(file,sheetName,r,2)
            email = xlUtiles.read_data(file, sheetName, r, 3)
            password = xlUtiles.read_data(file, sheetName, r, 4)

            self.reg.set_first_name(first_name)
            self.reg.set_last_name(last_name)
            #self.email = randon_string_generator(size=10) + "@gmail.com"
            self.reg.set_email(email)
            self.reg.set_password(password)
            self.reg.subscribe_newsletter()
            self.reg.accept_policy()
            time.sleep(5)
            self.reg.click_continue()
            actual_message = self.reg.get_confirmation_message()
            excepted_message ="Your Account Has Been Created!"
            if actual_message == excepted_message:
                xlUtiles.fill_green_color(file,sheetName,r,5)
                self.driver.back()
                self.driver.refresh()
                # assert True
            else:
                self.driver.save_screenshot(os.path.curdir+"\\screenshots\\TestRegisterFunctionalityTC001.png")
                xlUtiles.fill_red_color(file,sheetName,r,5)
                self.driver.refresh()
                # assert False
