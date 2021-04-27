import inspect
import logging


class LogGen:
    # LOG FORMAT
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\logs\\,testlog.log")  # , format='%(asctime)s: %(levelname)s:%(message)s',
        # datefmt='%m/%d/%Y %I:%M:%S %P')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    def loggingDmo(self, testname):
        # getLogger() method takes the test case name as input
        logger = logging.getLogger(__name__)
        # FileHandler() method takes location and path of log file
        fileHandler = logging.FileHandler('.\\logs\\,testlog.log')
        # Formatter() method takes care of the log file formatting
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :  % (name) s: % (message)  s ")
        fileHandler.setFormatter(formatter)
        # addHandler() method takes fileHandler object as parameter
        logger.addHandler(fileHandler)
        # setting the logger level

        logger.setLevel(logging.DEBUG)
        logger.debug("Debug log")
        logger.info("Information log ")
        logger.warning("Warning log")
        logger.error("Error log")
        logger.critical("Critical log")

        return logger

    def getLoger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('.\\logs\\,testlog.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :  %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger
