using NUnit.Framework;
using SeleniumFinalProject.Driver;
using SeleniumFinalProject.PageObject;
using SeleniumFinalProject.Tools;

namespace Tests
{
    public class Tests : WebDriver
    {
        FacebookLoginPage loginToFacebook = new FacebookLoginPage();
        Utilities report = new Utilities();

        [Test]
        public void logintoFaceBook_Test1()
        {
            report.Reports("Test_01","TestStarted");
            loginToFacebook.loginFaceBook();

        }
    }
}