using NUnit.Framework;
using System;
using System.Collections.Generic;
using System.Text;
using NUnit.Framework;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Firefox;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SeleniumFinalProject.Driver
{
    public class WebDriver
    {
        public static  IWebDriver driver;

        [SetUp]
        public void startBrowser()
        {
            driver = new ChromeDriver(System.IO.Path.GetDirectoryName(@"C:\chromedriver.exe"));
            driver.Url = "https://www.facebook.com/";
        }
       [TearDown]
        public void closeBrowser()
        {
            // driver.Close();

        }
    }

}