from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Screenshot():
    @staticmethod
    def takeScreenshot():
        screenshotpath = ".\\Screenshots\\" + "test_homePageTitle.png"
        return screenshotpath
