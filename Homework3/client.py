import sys
import argparse
from socket import *
import time
import json

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('address', default='localhost')
    parser.add_argument ('port', default=8007)
 
    return parser

# парсим параметры командной строки
parser = createParser()
params = parser.parse_args(sys.argv[1:])

s = socket(AF_INET, SOCK_STREAM)  # Создаем сокет TCP
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
s.send(json.dumps(msg).encode('utf-8'))
# принимаем ответ от сервера
data = s.recv(1000000)
print('Сообщение от сервера: ', data.decode('utf-8'), ', длиной ', len(data), ' байт')
s.close()