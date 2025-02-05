from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:

    txt_username_id = 'input-email'
    txt_password_id = 'input-password'
    btn_login_xpath ='//button[text()="Login"]'



    def __init__(self, driver):
        self.driver = driver


    def set_username(self,username):
        self.driver.find_element(By.ID,self.txt_username_id).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.ID,self.txt_password_id).send_keys(password)

    def click_login(self):
        WebDriverWait(driver=self.driver,timeout=10,poll_frequency=1).until(EC.element_to_be_clickable((By.XPATH,self.btn_login_xpath)))
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

