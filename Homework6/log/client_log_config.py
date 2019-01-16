
import logging
import inspect

# Создаем объект-логгер с именем client:
logger = logging.getLogger('client')

# Создаем объект форматирования:
formatter = logging.Formatter("<%(asctime)s> <%(levelname)s> <%(module)s> <%(message)s>")

# Создаем файловый обработчик логирования:
fh = logging.FileHandler("client.log", encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

# Добавляем в логгер новый обработчик событий и устанавливаем уровень логирования
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

def log(func):
    def call(*args, **kwargs):
        logger.debug('функция {} вызвана из фукции {}'.format(func.__name__, inspect.stack()[1][3]))
        return func(*args, **kwargs)
    return call

if __name__ == '__main__':
    # Создаем потоковый обработчик логирования (по умолчанию sys.stderr):
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logger.addHandler(console)
    logger.info('Тестовый запуск логирования')
