from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities.screenshot import Screenshot


class Test_001_Login(LogGen):
    # reading data from reading configobj
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPasword()
    # screenshotlocation
    screenshotpath = Screenshot.takeScreenshot()
    # variables:
    expPageTitel = "Facebook - Log In or Sign Up"

    def test_homePageTitle(self, setup):
        log = self.getLoger()
        log.info('__Test_0001__')

        # calling driver
        self.driver = setup
        self.driver.get(self.baseURL)
        page_title = self.driver.title
        assert page_title == self.expPageTitel

    def test_login(self, setup):
        log = self.getLoger()
        log.info('__Test_0001__')
        self.driver = setup
        self.driver.get(self.baseURL)
        # login test case
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clcikLogin()
        page_title = self.driver.title
        assert page_title == self.expPageTitel
