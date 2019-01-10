import sys
import argparse
from socket import *
import json

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-a', '--address', default='')
    parser.add_argument ('-p', '--port', default=8008)
 
    return parser

# парсим параметры
parser = createParser()
namespace = parser.parse_args(sys.argv[1:])

s = socket(AF_INET, SOCK_STREAM)
s.bind((namespace.address, int(namespace.port)))
s.listen()

while True:
    client, addr = s.accept()
    data = client.recv(1000000)
    clientMsg = json.loads(data)

    if clientMsg['action'] == 'presence':
        print('Сообщение: ', clientMsg['user']['status'], ', было отправлено клиентом: ', addr)
        msg = 'Привет, клиент'
    else:
        msg = 'Что то не так'
    client.send(msg.encode('utf-8'))
    client.close()
