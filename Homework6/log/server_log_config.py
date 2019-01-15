import logging
import logging.handlers
import inspect

# Создаем объект-логгер с именем server:
logger = logging.getLogger('server')

# Создаем объект форматирования:
formatter = logging.Formatter("<%(asctime)s> <%(levelname)s> <%(module)s> <%(message)s>")

# Создаем обработчик логирования с ежедневной ротацией в полночь и сохранением трех пред версий:
trfh = logging.handlers.TimedRotatingFileHandler('server.log', 
                                   encoding='utf-8',
                                   when='midnight',
                                   backupCount=3)

trfh.setLevel(logging.DEBUG)
trfh.setFormatter(formatter)

# Добавляем в логгер новый обработчик событий и устанавливаем уровень логирования
logger.addHandler(trfh)
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
