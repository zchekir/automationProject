from datetime import time

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.screenshot import Screenshot
from utilities import XLUtils
from locators import locator
import HTMLTestRunner


class Test_002_DDT_Login(LogGen):
    # reading data from reading configobj
    baseURL = ReadConfig.getApplicationURL()
    #Varibles
    excelpath = locator.path
    SheetID = 'Sheet1'
    ExPagetitle = "Facebook - Log In or Sign Up"
    ExPass = "Pass"
    ExFail = "Fail"
    lst_status = []  # empty list varibales
    screenshotpath = Screenshot()

    def test_login_ddt(self, setup):
        log = self.getLoger()
        log.info('__Test_0002__ExcelTestData__Started')

        # driver from setup mehod
        self.driver = setup
        self.driver.get(self.baseURL)
        # login test case
        lp = LoginPage(self.driver)

        # get the data from excel file
        rows = XLUtils.getRowCount(self.excelpath, self.SheetID)
        log.info( rows)

        for r in range(2, rows + 1):
            username = XLUtils.redData(self.excelpath, self.SheetID, r, 1)
            password = XLUtils.redData(self.excelpath, self.SheetID, r, 2)
            expResults = XLUtils.redData(self.excelpath, self.SheetID, r, 3)
            lp.setUserName(username)
            lp.setPassword(password)
            lp.clcikLogin()
            page_title = self.driver.title

            if page_title == self.ExPagetitle:
                if expResults == self.ExPass:

                    lp.clcikLogout();
                    self.lst_status.append(self.ExPass)
                    log.info('Test__02_ExcelTestData__Pass')



                elif expResults == self.ExFail:
                    log.info('__Test__02__ExcelTestData__Fail__')
                    lp.clcikLogout();
                    self.lst_status.append(self.ExFail)
                    self.driver.save_screenshot(self.screenshotpath.takeScreenshot())
                    self.driver.close()

        if self.ExFail in self.lst_status:
            log.info('TestFailed because one of the expected results failed')
        else:
            log.info('All The validation PASSED successfuly')


'''''

            elif page_title != "Facebook - Log In or Sign Up":
                if self.exp == "Pass":
                    self.lp.clcikLogout();
                    lst_status.append("Fail")
                    self.driver.close()


                elif self.exp == "Faill":
                    self.lp.clcikLogout();
                    lst_status.append("pass")

        if "Fail" not in lst_status:
            self.driver.close()
            assert True
        else:

            print("TESTfailed ")
            self.driver.close()
            assert False
'''''
