using System;
using System.Collections.Generic;
using System.Text;
using AventStack.ExtentReports;
using AventStack.ExtentReports.Reporter;
using NLog;

namespace SeleniumFinalProject.Tools
{
   public  class Utilities
    {
        ExtentReports extent = null;
        public void Reports(string testNumber, string info)
        {
            extent = new ExtentReports();
            var htmlReporter = new ExtentHtmlReporter(System.IO.Path.GetDirectoryName(@"C: \Users\zchekir\Desktop\logs\TestReport.html"));
            extent.AttachReporter(htmlReporter);
            extent.CreateTest(testNumber).Info(info);
        }

        public void Logs()
        {
             Logger logger = LogManager.GetLogger("mylogs");

        }

    }
}
