import sys
import argparse
from socket import *
import json
import logging
from log.server_log_config import *

logger = logging.getLogger('server')

@log
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-a', '--address', default='')
    parser.add_argument ('-p', '--port', default=8008)
 
    return parser

@log
def startServer():

    parser = createParser()
    params = parser.parse_args(sys.argv[1:])

    logger.debug('Создем сокет с ip: {}, port: {} и начинаем слушать входящшие сообщения'.format(params.address, int(params.port)))
    
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.bind((params.address, int(params.port)))
        s.listen()

        while True:
            client, addr = s.accept()
            data = client.recv(1000000)
            clientMsg = json.loads(data)

            if clientMsg['action'] == 'presence':
                logger.info('Сообщение: {}, было отправлено клиентом: {}'.format(clientMsg['user']['status'], addr))
                msg = 'Привет, клиент'
            else:
                msg = 'Что то не так'
            logger.debug('Отправляем сообщение клиенту: {}'.format(msg))
            client.send(msg.encode('utf-8'))
            client.close()
    except Exception as ex:
        logger.error(ex)
    

logger.debug('Запускаем сервер')
startServer()


