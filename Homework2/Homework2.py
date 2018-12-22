# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt
#  и формирующий новый «отчетный» файл в формате CSV. Для этого:
    # Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных. 
    # a. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы».
    #    Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
    #    В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка:
    #    «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
    # b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных через вызов функции get_data(),
    #    а также сохранение подготовленных данных в соответствующий CSV-файл;
    # c. Проверить работу программы через вызов функции write_to_csv().
# import re
# import os
# import csv

# def get_data():
#     fileNameReg = re.compile(r'info_(\d+).txt')
#     systemManufacturer = re.compile(r'Изготовитель системы:(.*)')
#     osName = re.compile(r'Название ОС:(.*)')
#     codeProduct = re.compile(r'Код продукта:(.*)')
#     systemType = re.compile(r'Тип системы:(.*)')

#     os_prod_list = []
#     os_name_list = []
#     os_code_list = []
#     os_type_list = []

#     # читаем файлы в папке
#     for filename in os.listdir('Homework2'):
#         if(fileNameReg.match(filename)):
#             with open("Homework2/" + filename,"r", encoding="windows-1251") as f:
#                 line = next(f)
#                 while line:
#                     if systemManufacturer.match(line):
#                         os_prod_list.append(systemManufacturer.match(line).group(1).strip())
#                     if osName.match(line):
#                         os_name_list.append(osName.match(line).group(1).strip())
#                     if codeProduct.match(line):
#                         os_code_list.append(codeProduct.match(line).group(1).strip())
#                     if systemType.match(line):
#                         os_type_list.append(systemType.match(line).group(1).strip())


#                     line = next(f, None)

#     main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

#     # не совсем понял зачем нам нужны четыре отдельных списка чтобы собрать в один. Здесь я допуская что длина всех списков одинаковая :)
#     for i in range(len(os_prod_list)):
#         main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])

#     return main_data

# def write_to_csv(fileName):
#     with open(fileName, 'w', encoding='UTF-8') as f:
#         f_writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
#         f_writer.writerows(get_data())


# write_to_csv('Homework2/report.csv')

# 2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для этого:
# a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
#  Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
# b. Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
# import json

# def write_order_to_json(item, quantity, price, buyer, date):
#     with open("Homework2/orders.json", "r") as f:
#         data = json.load(f)
#     data["orders"].append({'item' : item, 'quantity' : quantity, 'price':price, 'buyer': buyer, 'date': date })

#     with open("Homework2/orders.json", "w") as f:
#         json.dump(data, f, indent=4)

# write_order_to_json('test', 'test1', 'test2', 'test4', 'test5')
# write_order_to_json('sdfsd', '435435', 'tsdfsdfest2', '4545', 'sdfsdf')


# 3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
#   a. Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число, третьему — вложенный словарь,
#  где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке ASCII (например, €);
#   b. Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
#  а также установить возможность работы с юникодом: allow_unicode = True;
#   c. Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
import yaml

data = {'key1': ['test', 'test1'], 'key2': 300, 'key3': {'usd': '70$', 'eur': '100€'} } 

with open('Homework2/file.yaml', 'w', encoding='UTF-8') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)

