from selenium.webdriver.common.by import By


class locator:

    #LoginPage:-------------------------------------------------
    textbox_username_xpath = "body.user-type-iam.awsui-mezzanine-overrides:nth-child(2) div.awsc-pad-top-below-h-imp.awsc-pad-bot-above-f-imp:nth-child(2) div.awsui div.awsui.awsui-dense-table div.awsui-app-layout.awsui-app-layout-contentType-default main.awsui-app-layout__container div.awsui-app-layout__content div.awsui-app-layout__content--scrollable div.s3-objects-view-container div.bucket-details div.awsui-tabs-variant-default div.awsui-tabs-content-wrapper div.awsui-tabs-content.awsui-tabs-content-active:nth-child(1) div.objects-list-table awsui-table.objects-list-table--unversioned div.awsui-table-inner.awsui-table-variant-default div.awsui-table-container tr.awsui-table-row:nth-child(1) span:nth-child(1) span.column-Name span.object-link a:nth-child(2) > span.name.object.latest.object-name"
    textbox_password_xpath = "//input[@id='pass']"
    button_login_xpath = "//*[@name='login']"
    # logout
    button_logout1_xpath = "//*[@aria-label='Account']"
    button_logout2_xpath = " // span[contains(text(), 'Log Out')]"

    # Homepage Locators:-------------------------------------------
    textbo_searshFacebook_xpath =  "//input[@type='search']"

    # ExcelTestdata
    path = "C:/Users/zchekir/Desktop/testDatat.xlsx"