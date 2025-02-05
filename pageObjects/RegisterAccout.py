import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterAccount:

    text_firstName_xpath = '//input[@id="input-firstname"]'
    text_lastName_xpath = '//input[@id="input-lastname"]'
    text_email_xpath = '//input[@id="input-email"]'
    text_password_xpath = '//input[@id="input-password"]'
    button_newsletterSubscribe_xpath = '//input[@id="input-newsletter"]'
    button_acceptPolicy_xpath = '//input[@name="agree"]'
    button_continue_xpath = '//button[text()="Continue"]'
    text_confirmationMsg_xpath = '//h1[text()="Your Account Has Been Created!"]'


    def __init__(self,driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()

    def set_first_name(self,first_name):
        self.driver.find_element(By.XPATH,self.text_firstName_xpath).send_keys(first_name)

    def set_last_name(self,last_name):
        self.driver.find_element(By.XPATH,self.text_lastName_xpath).send_keys(last_name)

    def set_email(self,email):
        self.driver.find_element(By.XPATH,self.text_email_xpath).send_keys(email)

    def set_password(self,password):
        self.driver.find_element(By.XPATH,self.text_password_xpath).send_keys(password)

    def subscribe_newsletter(self):

        element = self.driver.find_element(By.XPATH, self.button_newsletterSubscribe_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)
        WebDriverWait(driver=self.driver,timeout=10,poll_frequency=2).until(EC.element_to_be_clickable(element))
        element.click()


    def accept_policy(self):
        element=self.driver.find_element(By.XPATH,self.button_acceptPolicy_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(driver=self.driver, timeout=10, poll_frequency=2).until(EC.element_to_be_clickable(element))
        element.click()

    def click_continue(self):
        btn = self.driver.find_element(By.XPATH, self.button_continue_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        WebDriverWait(driver=self.driver, timeout=10, poll_frequency=2).until(EC.element_to_be_clickable(btn))
        btn.click()

    def get_confirmation_message(self):
        try:
            message = self.driver.find_element(By.XPATH,self.text_confirmationMsg_xpath).text
            return  message
        except:
            None


