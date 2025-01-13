# ! Во время импорта весь код из файла исполняется
# Однако, это происходит только при первом импорте нового модуля
# В питоне существует такой объект sys.modules (словарь), в котором указаны объекты всех модулей, к ним можно обратится через ключ по имени
# При встречи имени модуля, которого нет в ключах файл в модуле исполняется и создаётся объект, который мы записываем в словарь sys.modules
# При повторной встречи с импортом того же модуля возьмётся уже созданный ранее объект модуля из sys.modules\

# import sys
# print(sys.modules)                      # вот этот словарь

# Если модуля нет в словаре, питон ищет его в текущей директории, если и там его нет то в внешних библиотеках (там он и находит все базовые а также скачанные библиотеки)

# Импортировать можно и пакеты (папки с множеством файлов, которые ведут себя как модуль), однако для этого нужна дополнительная возня

# Program
# from datetime import datetime, timedelta,date
# x = input().split(' ')
# time = date(year=int(x[0]),month=int(x[1]), day=int(x[2]))
#
# new_time = time + timedelta(days=int(input()))
# new_time = ' '.join([str(int(i)) for i in str(new_time).split('-')])
# print(new_time)

# При помощи конструкции 'from ... import *' мы можем импортировать все имена из модуля
# !!! НО если в модуле, который мы импортируем добавить список __all__ = [], в котором указать все имена, которые мы хотим импортировать вместе с модулем,
                                                                                                            # то при импорте со звёздочкой будут перенесены ТОЛЬКО эти имена!
# ! Имена, которые начинаются с '_' никогда не будут переноситься вместе со звёздочкой !

# Final Program
# import simplecrypt
# list = []
# with open(r"C:\Users\danny\Downloads\encrypted.bin", "rb") as inp:
#     encrypted = inp.read()
# with open(r'C:\Users\danny\Downloads\passwords.txt', 'r') as file:
#     for i in range(10):
#         list.append((file.readline()).replace('\n', ''))
#
# print(list)
# for line in list:
#     try:
#         a = simplecrypt.decrypt(line, encrypted).decode('utf8')
#         print(a)
#     except:
#         pass
