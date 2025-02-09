import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\91992\\PycharmProjects\\OHRM_101\\Configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def GetUsername():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def GetPassword():
        password = config.get('common data', 'password')
        return password
