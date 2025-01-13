# def checkio(data,repeater):                 # Выводит все повторяющиеся объекты (repeater - число раз которое объект должен повторять)
#     result = []
#     for i in data:
#         n = 0
#         for j in data:
#             if i == j :
#                 n += 1
#                 if n == repeater:
#                     result.append(j)
#                     break
#     return result
# print(checkio([10, 9, 10, 10, 9, 8],2))
#
# def popular_words(text, words):
#     text, result = text.lower(), {}
#     text = text.split()
#     for n in words:
#         result[n] = text.count(n)           # !!! Способ вносить данные в словарь, Метод list.count("object") - позволяет легко подсчитать кол-во "object" в list
#     return result
#
#
# def frequency_sort(items):                      # Cортировка объектов по их частоте в строке
#     dict ={item : items.count(item) for item in items}
#     list_dict = list(dict.items())
#     list_dict.sort(key=lambda i: i[1], reverse = True)
#     dict_2 = {i[0] : i[1] for i in list_dict}
#     return [key for key in dict_2.keys() for i in range(dict_2[key])]
# print(frequency_sort([4,6,2,2,2,6,4,4,4]))
#
#
# def morse_decoder(code):                        # Шифровка и расшифровка азбукой МОРЗА
#     MORSE = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h", "..": "i",
#              ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r",
#              "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z", "-----": "0",
#              ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9", "":""}
#     code = code.replace("#","")
#     if code.count('-') + code.count('.') + code.count(' ') == len(code):
#         code = code.split("   ")
#         result = ''
#         for j in range(len(code)):
#             for i in code[j].split(" "):
#                 result += MORSE[i]
#             result += " "
#         return result.strip().capitalize()
#     else:
#         MORSE = { value : key for key, value in MORSE.items()}
#         code = code.lower()
#         code, result =  code.split(" "), ""
#         for j in range(len(code)):
#             for i in code[j]:
#                 try:
#                     result+= MORSE[i] + " "
#                 except KeyError:
#                     result+= "#"
#             result += "  "
#         return result.strip()
# print(morse_decoder("###    ... --- -- .   - . -..- - -.- . -.-- . .-. .-. --- .-."))
#
#
# # Работает с unicode
# import unicodedata                  # НЕпонятная библиотека
# def checkio(in_string):             # Программа не моя!         (Заменяет все непонятные символы на их аналоги)
#     return "".join([ i for i in unicodedata.normalize('NFD', in_string) if unicodedata.category(i) != 'Mn'])
# print(checkio(u"préfèrent"))
#
# # Заменяет все пробелы на "_" в указанной папке
# import os
# PATH = r'C:\Users\danny\Music\{}'
# list = os.listdir(r'C:\Users\danny\Music')
# for file in list:
#     renamed_file = file.replace(' ', '_')
#     os.rename(PATH.format(file), PATH.format(renamed_file))
#
#
#
#
# # Лёгкий способ хранения переменной в файле (если надо, чтобы изменения при работе с программой сохранялись и при перезапуске программы)
# import pickle
# # Запись
# Something = {"HAZBIN_HOTEL_-_Alastor's_Game_[ROCK_Song.mp3"}
# with open(r'D:\Программирование\Python начало\Jack_PersonalAssistant\Не_трогать(костыль)\Something.pickle', 'wb') as f:
#     pickle.dump(Something, f)
# # Чтение
# with open(r'D:\Программирование\Python начало\Jack_PersonalAssistant\Не_трогать(костыль)\Something.pickle', 'rb') as f:
#     Something = pickle.load(f)
# print(Something)

# # Выводит Страну по указанным координатам (работает плохо, не советую использовать!)
# from pyowm.owm import OWM
# owm = OWM('265149b85a7e21285e992960b1a681c8')
# mgr_forC = owm.geocoding_manager()
#
# lat, lon = 47.000107, 28.865851
#
# list_of_locations = mgr_forC.reverse_geocode(lat, lon)
# print(list_of_locations[0].name)


# # Определение самой длинной подстроки для двух строк (из Грокаем Алгоритмы с 234-235)
# # !!! Моя версия работает ЛУЧШЕ, чем книжная !!!
#
# word1 = 'fair'
# word2 = 'affair'
#
# cell = [[0 for j in range(len(word1))] for i in range(len(word2))]              # заполняем строку столбцами (в таблице)
#
# for i in range(len(cell)):                                          # Пробегаем по каждой строке
#     for j in range(len(cell[0])):                                                # По каждому столбцу данной строки
#         if word1[j] == word2[i]:
#             cell[i][j] = cell[i-1][j-1] + 1
#         else:
#             cell[i][j] = cell[i-1][j-1] + 0
# for string in cell:
#     print(string)
#
# maximum = 0
# for string in cell:
#     if max(string) > maximum:
#         maximum = max(string)
#
# print(maximum)