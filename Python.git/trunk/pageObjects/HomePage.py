from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from locators import locator


class HomePage():

    def __init__(self, driver):
        self.driver = driver

    # xpaths
    textbo_searshFacebook = (By.XPATH, locator.textbo_searshFacebook_xpath)

    def searshFacebook(self, name):
        self.driver.find_element(*HomePage.textbo_searshFacebook).clear()
        self.driver.find_element(*HomePage.textbo_searshFacebook).send_keys(name)
        self.driver.find_element(*HomePage.textbo_searshFacebook).send_keys(Keys.ENTER)
