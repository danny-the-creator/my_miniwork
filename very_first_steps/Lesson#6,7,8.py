# print(type(a))                              # type() - показывает класс объекта в скобках  (int, float, string...)

# tuple_1 = (12,23.48,"Hi!",)                # (картедж) как список, только нельзя ИЗМЕНИТЬ (","(которая в конце)-позволяет верно определить тип (Она просто нужна, неважно))
# print(tuple_1)
# spisok = [12,12,12];print(spisok)
# print(tuple(spisok))                         # превращает список в картедж
# spisok = list(spisok); print(spisok)        # превращает картедж в список

dict = {"гелий":'газ', "Вода":'жидкость', "Железо":'Твёрдое тело', "Метан":'газ',}      # dict(словарь) - как списки, только вместо индексов - КЛЮЧИ
# print(dict.keys())                   # .keys()     КЛЮЧИ(index) - "гелий", "Вода", "Железо", "Метан"
# print(dict.values())                 # .values()   ЗНАЧЕНИЯ(данные) - 'газ', 'жидкость', 'Твёрдое тело', 'газ'
# print(dict["гелий"])                    # [key] - элемент которому соответствует этот ключ

# dict["гелий"] = "Жидкость"              # можно заменять
# print(dict)

# del(dict["гелий"]); print(dict)             # del - удалить


# "\t" - одна табуляция в строке

# text = "Good luck Commander!"
# text_1 = (text[0:9] + text[-1]); print(text_1)            # Вывод символов от "0"(входит) до "9"(НЕ входит)
# # можно выводить с конца, если ввести отрицательное значение
# print(text_1.upper())                           # Всё Caps Lock-ом
# text_2 = (text_1.lower()); print(text_2)        # Всё строчными
# print(text_2.capitalize())                      # C заглавной

# sentence = "Беспроводные наушники     Sony WI-C200 White"
# split = sentence.split(" ")                 # Cоздаёт список из строки (в кавычкач указывается символ который будет делить строку)
# print(split)                                # Делящий символ выводиться НЕ будет!
# # Обратная операция - "_".join(spisok) - соединяет список в строку, между каждым элементом будет выводить то, что в "_"
# x = "     f f  f         f              "
# print(x.strip())                            # удаляет все "_" в начале и конце строки\
# Text ="alalalalalallaalaalaalalla"
# print(Text.replace("l","o"))                # заменяет все "l" на "o"

# import math as m                            # писать в начале, импортирует строрнний модуль, m - cокращённое имя модуля
# print(m.pi)                                 # "Name of Module"."function" (m.pi)
# from math import pi as p                # Импорт одной функции, остальные не доступны, можно использовать сразу "function" без "Name of Module".
# from math import *                      # Импорт всех объектов модуля
# import test_678 as t                    # import another file from my project (test_678)    (Нужно правильно называть файлы или импорт будет невозможен!)
# t.hello()                               # usage function from my project (test_678)