import csv                                  # csv - формат текста, в котором каждая новая строка это ряд, элементы которого перечислены через запятую (!без скобок)
                                                                    # Поэтому этот формат имеет вид таблицы, и для чтения файла с таким форматом есть своя отдельная библиотека(scv)
# Формат: один, два, три                            Вывод: [один, два, три]
# четыре, пять, шесть                               [четыре, пять, шесть]

# ! Если нам нужно передать '\n' или ',' в качестве элемента таблицы, этот элемент нужно заключить в ""

# with open('file.csv') as file:
#     result = csv.reader(file)               # Таким образом можно считать файл, также можно указать delimiter (делитель вместо стандартной запятой)
#     for row in result:                                                              # (тогда нужно менять формат csv на какой-то другой...)  Схожим образом можно заменить и знак ""
#         print(row)
#
# with open('file.csv') as file:
#     writer = csv.writer(file)
#
#     for element in list:                                # Для каждого элемента списка записывает его через запятую в файл
#         writer.writerow(element)  # имеет атрибуд 'quoting', в который подставляются некоторые константы модуля, и который вляет на некоторые элементы, которые нужно записать в ""
#
#     writer.writerows(list)                               # Аналогичная урощённая запись верхнего цикла

# First Program
# import csv
# crimes_list = []
# with open(r'C:\Users\danny\Downloads\Crimes.csv') as file:
#     result = csv.reader(file)
#     for i in result:
#         # print(i[2][6:10])                                      # [5] - Primary Type         [2][6:10] - Date Year
#         if i[2][6:10] == '2015':
#             crimes_list.append(i[5])
#
# crimes_set = set(crimes_list.copy())
# crimes_set = [(crimes_list.count(crime), crime) for crime in crimes_set]
# crimes_set.sort(reverse=-1)
# # print(crimes_set)
# print(crimes_set[0][1])

import json                         # json - формат, который содержыт объекты javascript (выглядят как словари питона, но ключ - только строка в "" ( !не ' )
                                                                                                                    #  True, False, None = true, false, null)
                                    # модуль 'json' позволяет удобно считывать и записыват файлы, не парясь наcчёт отличия питона и js (чаще всего модуль записывает список словарей)

# object1 = {'fff':3,
#            'numbder': 8,
#            'smart' : False}
# object2 = {'^&Rfg': None,
#            'number' : 42,
#            'smart' : True}
#
# data = [object1, object2]           # список объктов (список словарей)
#
# import json
# js = json.dumps(data, indent=7, sort_keys=True)                         # метод 'dumps' переводит данные в json формат (indent - кол-во отступов)
# print(js)                                                                                                                   # (изменяя и подстраивая данные под него)
# # чтобы записать в файл нужно использовать метод 'dump' и добавить вторым значением имя файла записи (!!!не забыть:  with open(file) as f: ...)
#
# # Обратный метод от dump и dumps - load, loads                          # используя эти методы мы получим объект, который будет копией нашей 'data', из формата json
#
# data = json.loads(js)                                                   # Формат Записи

# Final Program
# import json
#
# def generation(name, count):
#     global checked
#     for object in data:
#         parents = object['parents']
#         son_name = object['name']
#         if name in parents and son_name not in checked:
#             count += 1
#             count = generation(name=son_name, count=count)
#     checked.append(name)
#     return count
#
# data = json.loads(input())
#
# data.sort(key=lambda x:x['name'])
# print(data)
#
# for i in range(len(data)):
#     element = data[i]
#     name = element['name']
#     checked = []
#     count = generation(name, count=1)
#
#
#     print(f'{name} : {count}')