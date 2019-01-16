import sys
import argparse
from socket import *
import time
import json
import logging
import log.client_log_config

logger = logging.getLogger('client')


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('address', nargs='?', default='localhost')
    parser.add_argument ('port', nargs='?', default=8008)
 
    return parser

def sendPresence ():
    # парсим параметры командной строки
    logger.debug('Парсим параметры командной строки')
    parser = createParser()
    params = parser.parse_args(sys.argv[1:])

    logger.debug('Создаем сокет TCP и пытаемся подключиться к серверу ip: {} port: {}'.format(params.address, int(params.port)))
    s = socket(AF_INET, SOCK_STREAM)  # Создаем сокет TCP
    try:
        s.connect((params.address, int(params.port)))   # Соединяемся с сервером
        # presence-сообщение
        msg = {
                "action": "presence",
                "time": time.time(),
                "type": "status",
                "user": {
                        "status":      "Hello"
                }
        }
        # отправляем запрос
        logger.debug('Отправляем запрос: {}'.format(json.dumps(msg).encode('utf-8')))
        s.send(json.dumps(msg).encode('utf-8'))
        # принимаем ответ от сервера
        data = s.recv(1000000)
        logger.info('Сообщение от сервера: {}, длиной {} байт'.format(data.decode('utf-8'), len(data)))
        s.close()
    except Exception as ex:
        logger.error(ex)
    

logger.debug('Старт приложения')

sendPresence()

