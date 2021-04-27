from selenium import webdriver
from selenium.webdriver.common.by import By

from locators import locator


class LoginPage:

    # driver instance in order to pass the driver from test_login to loginpage
    def __init__(self, driver):
        self.driver = driver

    # xpaths
    textbox_username_xpath = (By.CSS_SELECTOR, locator.textbox_username_xpath)
    textbox_password_xpath = (By.XPATH, locator.textbox_password_xpath)
    button_login_xpath = (By.XPATH, locator.button_login_xpath)
    button_logout1_xpath = (By.XPATH, locator.button_logout1_xpath)
    button_logout2_xpath = (By.XPATH, locator.button_logout2_xpath)

    def setUserName(self, username):
        self.driver.find_element(*LoginPage.textbox_username_xpath).click()
        self.driver.find_element(*LoginPage.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(*LoginPage.textbox_password_xpath).clear()
        self.driver.find_element(*LoginPage.textbox_password_xpath).send_keys(password)

    def clcikLogin(self):
        self.driver.find_element(*LoginPage.button_login_xpath).click()

    def clcikLogout(self):
        self.driver.find_element(*LoginPage.button_logout1_xpath).click()
        self.driver.find_element(*LoginPage.button_logout2_xpath).click()
