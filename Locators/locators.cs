using System;
using System.Collections.Generic;
using System.Text;

namespace SeleniumFinalProject.Locators
{
    public class Locator
    {
        // Login page Object

        public string userName = "//input[@id='email']";
        public string passWord = "//input[@id='pass']";
        public string logIn = "//*[@name='login']";
    }
}
