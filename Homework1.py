str1, str2, str3  = 'разработка', 'сокет', 'декоратор'

print(str1, str2, str3)
print(type(str1), type(str2), type(str3))

str1, str2, str3  = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', '\u0441\u043e\u043a\u0435\u0442', '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
print(str1, str2, str3)
print(type(str1), type(str2), type(str3))

str1, str2, str3 = b'class', b'function', b'method',
print(str1, str2, str3)
print(type(str1), type(str2), type(str3))
print(len(str1), len(str2), len(str3))

str1 = b'attribute'
# str2 = b'класс'
# str3 = b'функция'
str4 = b'type'


str1, str2, str3, str4  = 'разработка', 'администрирование', 'protocol', 'standard'

b1, b2, b3, b4 = str1.encode(), str2.encode(), str3.encode(), str4.encode()
print(b1, b2, b3, b4)
print(b1.decode(), b2.decode(), b3.decode(), b4.decode())

import os
ping1, ping2 = os.popen('ping youtube.com').read(), os.popen('ping yandex.ru').read()

print(ping1)
print(ping2)

f= open("test.txt","w+", encoding="UTF-8")

strs = ['сетевое программирование', 'сокет', 'декоратор']
for i in range(len(strs)):
    f.write(strs[i] + '\n')

f = open("test.txt","r")
print(f)
f = open("test.txt","r", encoding = 'UTF-8')

print(f.read())