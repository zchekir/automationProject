import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import HTMLTestRunner

driver = None
#### setting the driver
@pytest.fixture()
def setup(browser):
    global driver
    option = Options()
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2
    })
    if browser =='chrome':

        driver = webdriver.Chrome(chrome_options=option,executable_path="C://chromedriver.exe")

    elif browser== 'firefox':
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    else:
        driver = webdriver.Ie()

    driver.implicitly_wait(200)
    driver.maximize_window()
    if __name__ == "__main__":
        HTMLTestRunner.main()
    return driver

### runing wiht multi browser
# runing a test with different browser HOKS
def pytest_addoption(parser):
    # this for configuring the script to accept a user browser input
    parser.addoption("--browser", action="store", default="chrome")

# runing a test with different browser
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

### HTML REPORT coSMAZATION ###
'''''
def pytest_configure(config):
    config.metadata['ProjectName']='hybridFramework'
    config.metadata['ModuletName'] = 'Facebook'
    config.metadata['Tester'] = 'ZAK'
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
'''''
#hooke for capturing a screenshot when test failed and show in in the HTML Report
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail) :
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
