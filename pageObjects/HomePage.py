from selenium.webdriver.common.by import By

class HomePage:

    link_myAccount_xpath = '//span[text()="My Account"]'
    link_register_xpath = '//*[text()="Register"]'
    link_login_xpath  = '//*[text()="Login"]'


    def __init__(self,driver):
        self.driver = driver


    def click_my_account(self):
        self.driver.find_element(By.XPATH,self.link_myAccount_xpath).click()

    def click_register(self):
        self.driver.find_element(By.XPATH,self.link_register_xpath).click()

    def click_login(self):
        self.driver.find_element(By.XPATH,self.link_login_xpath).click()



