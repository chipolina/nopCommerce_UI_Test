import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


# Читаем данные из файлы config.ini
class ReadConfig:
    @staticmethod
    def getUrl():
        url = config.get('config', 'url')
        return url

    @staticmethod
    def getEmail():
        email = config.get('config', 'email')
        return email

    @staticmethod
    def getPassword():
        password = config.get('config', 'password')
        return password

    @staticmethod
    def getPassword_error():
        password_error = config.get('config', 'password_error')
        return password_error
