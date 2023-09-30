import datetime as dt
from colorama import init, Fore
from abc import ABC, abstractmethod

init(autoreset=True)

class Logger(ABC):
    @abstractmethod
    def info(self, message, object): pass

    @abstractmethod
    def warning(self, message, object): pass

    @abstractmethod
    def error(self, message, object): pass

    @abstractmethod
    def debug(self, message, object): pass

class LoggerConsole(Logger):
    def info(self, message, object):
        print(f'{dt.datetime.now()} {Fore.BLUE} [INFO] {message, object}')

    def warning(self, message, object):
        print(f'{dt.datetime.now()} {Fore.YELLOW} [WARNING] {message, object}')

    def error(self, message, object):
        print(f'{dt.datetime.now()} {Fore.RED} [ERROR] {message, object}')

    def debug(self, message, object):
        print(f'{dt.datetime.now()} {Fore.MAGENTA} [DEBUG] {message, object}')

log_file = 'file.log'
class LoggerFile(Logger):
    def info(self, message, object):
        with open(log_file, 'a') as file:
            data = f'{str(dt.datetime.now())} [INFO] {message, str(object)}\n'
            file.writelines(data)

    def warning(self, message, object):
        with open(log_file, 'a') as file:
            data = f'{str(dt.datetime.now())} [WARNING] {message, str(object)}\n'
            file.writelines(data)

    def error(self, message, object):
        with open(log_file, 'a') as file:
            data = f'{str(dt.datetime.now())} [ERROR] {message, str(object)}\n'
            file.writelines(data)

    def debug(self, message, object):
        with open(log_file, 'a') as file:
            data = f'{str(dt.datetime.now())} [DEBUG] {message, str(object)}\n'
            file.writelines(data)

class LoggerEmail(Logger):
    def info(self, message, object):
        print(f'Mail [INFO] {message, object}')

    def warning(self, message, object):
        print(f'Mail [WARNING] {message, object}')

    def error(self, message, object):
        print(f'Mail [ERROR] {message, object}')

    def debug(self, message, object):
        print(f'Mail [DEBUG] {message, object}')

class LoggerFactory(ABC):
    @abstractmethod
    def get_logger(self, type): pass

class LoggerFactoryImpl(LoggerFactory):
    def get_logger(self, type) -> Logger:
        dic = {
            'c':LoggerConsole(),
            'f':LoggerFile(),
            'e':LoggerEmail()
        }
        return dic[type]

def main() -> None:
    while True:
        type_logger = str(input("""
[c] Para salida por consola
[f] Para salida por archivo
[e] Para salida por email
>>> """))
        logger = LoggerFactoryImpl().get_logger(type=type_logger)
        logger.info('Mensage genérico', 200)
        logger.warning('Mensage genérico', 404)
        logger.error('Mensage genérico', 401)
        logger.debug('Mensage genérico', 500)
        if type_logger == 'a':
            break

if __name__ == '__main__':
    main()