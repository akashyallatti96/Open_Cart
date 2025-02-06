import configparser
import os.path

config = configparser.RawConfigParser()
config.read(r"E:\Selenium_Project\Open_Cart\configurations\config.ini")

class ReadConfig():
    @staticmethod
    def get_app_url():
        url = (config.get("commonInfo","baseURL"))
        return url

    @staticmethod
    def get_username():
        username = (config.get("commonInfo","username"))
        return username

    @staticmethod
    def get_password():
        password = (config.get("commonInfo","password"))
        return password

    @staticmethod
    def get_login_URL():
        login_url = config.get("commonInfo","login_URL")
        return login_url