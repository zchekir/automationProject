
import time

from pageObjects.HomePage import HomePage
from testCases import test_login
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities.screenshot import Screenshot


class Test_002_Homepage(LogGen):
    screenshotpath = Screenshot()
    users = ReadConfig.getusers()
    #caling logintest cases
    login = test_login.Test_001_Login()

    def test_facebookserach(self, setup):
        log = self.getLoger()
        log.info('____Tests_002__Started____')
        self.driver = setup
        self.login.test_login(setup)
        time.sleep(2)
        homepage = HomePage(self.driver)
        homepage.searshFacebook(self.users)
        self.driver.save_screenshot(self.screenshotpath.takeScreenshot())
        self.driver.close()
        log.info('____Test02__ended____')

