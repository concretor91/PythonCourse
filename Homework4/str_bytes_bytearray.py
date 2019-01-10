# В Python 3 все строки - строки юникода
s = 'Python'

# Отдельный тип - строка байтов
bs = b'Python'

# Отдельный тип - bytearray - изменяемая строка байтов
ba = bytearray(bs)

def DecodeByteToStr(bs, charset):
    return bs.decode(charset)

def EncodeStrToBytes(s, charset):
    return s.encode(charset)  

def StrToBytearrray(s, charset):
    return bytearray(s, charset) 

# Преобразования между строками
s2 = DecodeByteToStr(bs, 'cp1251')        # Из байт-строки в юникод строку
bs2 = EncodeStrToBytes(s, 'koi8-r')        # Из юникод-строки в строку байтов
ba2 = StrToBytearrray(s, 'utf-8')    # Из юникод-строки в массив байтов

print(ba2)