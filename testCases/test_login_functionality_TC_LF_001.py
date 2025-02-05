import time

import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class Test_LOGIN_FUNCITONALITY_TC_LF_001:


    @pytest.mark.regression


    def test_login_TC_LF_001(self,setup):
        self.driver  = setup
        self.driver.get(ReadConfig.get_login_URL())

        self.lp =LoginPage(self.driver)
        self.lp.set_username('yixerzfvdh@gmail.com')
        self.lp.set_password('abcdefg')
        time.sleep(5)
        self.lp.click_login()
        time.sleep(2)
        assert "My Account" == self.driver.title


