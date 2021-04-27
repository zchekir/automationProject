import configparser

config = configparser.RawConfigParser()
config.read(".\\Confugurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPasword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getusers():
        password = config.get('test data', 'users')
        return password
