using System;
using System.Collections.Generic;
using System.Text;
using SeleniumFinalProject.Driver;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using SeleniumFinalProject.Locators;
using SeleniumFinalProject.TestData;

namespace SeleniumFinalProject.PageObject
{
    class FacebookLoginPage: WebDriver
    {

        //varibles:
        public Locator xpath = new Locator();
        public Credentials crednetials = new Credentials();

        public void loginFaceBook()
        {
            
            IWebElement enterUserName = driver.FindElement(By.XPath(xpath.userName));
            enterUserName.SendKeys(crednetials.userName);

            IWebElement enterPassword = driver.FindElement(By.XPath(xpath.passWord));
            enterPassword.SendKeys(crednetials.userName);

            IWebElement clickLogin = driver.FindElement(By.XPath(xpath.logIn));
            clickLogin.Click();

            
        }

       


    }
}
