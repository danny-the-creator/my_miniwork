#1
# def sum_numbers(text):
#     text = text.split(" ")
#     summ = 0
#     for i in text:
#         try:
#             summ += int(i)
#         except:
#             summ = summ
#     return summ
# print(sum_numbers("1223  333g"))

#1 Лучший вариант
# def sum_numbers(text: str) -> int:
#     return sum(int(word) for word in text.split() if word.isdigit())

#2
# def checkio(list):
#     summ = 0
#     if list != []:
#         for i in list[::2]:
#             summ += i
#         summ = summ * list[-1]
#     return summ
# print(checkio([6, 5, 3]))


# #3
# import re
# def checkio(words):
#     words = words.split(" ")
#     words = [i for i in words if len(i) != 0]
#     n = 0
#     for i in words:
#         a = re.search(r"\d",i)
#         if a != None:
#             n = -1
#         n += 1
#         if n >= 3:
#             return n >= 3
#     return n >= 3
# print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))
#
# #3 Лучший вариант
# import re
# def checkio(words):
#     return bool(re.compile("([a-zA-Z]+ ){2}[a-zA-Z]+").search(words))

# 4
# import re
# def first_word(text):
#     return str(re.search(r"\w{1,}'\w{1,}|\w{1,}", text)[0])
# print(first_word("greeting's, friends"))



#5- НЕ моё!
# Don't invent bicycle, Python has libraries to work wit date in time. Read about datetime, date and timedelta.
# from datetime import date                     # Библиотеки, что упращают жизнь при работе с разницой во времени  !!!
# def days_diff(a, b):
#     f = date(*a)# 31 december 2014
#     s = date(*b) # 1 january 2011
#     result = (f - s).days
#     if result < 0:
#         result *= -1
#     return result
# print(days_diff((1982, 4, 19), (1982, 4, 22)))

#6
# def count_digits(text):
#     n = 0
#     for i in text:
#         if i in {'0','1','2','3','4','5','6','7','8','9'}:
#             n += 1
#     return n
# print(count_digits('''This picture is an oil on canvas
#  painting by Danish artist Anna
#  Petersen between 1845 and 1910 year'''))


#7
# def backward_string_by_word(text):
#     text = text.split(" ")
#     j = 0
#     for i in text:
#         text[j] = i[::-1]
#         j += 1
#     return " ".join(text)
# print(backward_string_by_word('hello              world'))

#8
# def bigger_price(limit, data):
#     result = {}
#     result = sorted(data, key=lambda x: x['price'], reverse=True)
#     return result[:limit]
# print(bigger_price(2, [
#     {"name": "bread", "price": 100},
#     {"name": "wine", "price": 138},
#     {"name": "meat", "price": 15},
#     {"name": "water", "price": 1}
# ]))

#9
# import re
# def left_join(phrases):
#     phrases = ",".join(phrases)
#     return re.sub(r"right", "left",phrases)
# print(left_join(("bright aright", "ok")))

#10
# def between_markers(text, begin, end):
#     a, b = len(begin), 0
#     if begin not in text:
#         begin = text[0]
#         a = 0
#     if end not in text:
#         end = text[-1]
#         b = 1
#     return text[text.index(begin)+a:text.index(end) + b]
# print(between_markers('What is apple', '.>', '.<'))

#11
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

#12
# def popular_words(text, words):
#     text, result = text.lower(), {}
#     text = text.split()
#     for n in words:
#         result[n] = text.count(n)           # !!! Способ вносить данные в словарь, Метод list.count("object") - позволяет легко подсчитать кол-во "object" в list
#     return result

# 13
# def second_index(text, symbol):
#     n = j = 0
#     for i in text:
#         if i == symbol:
#             n+=1
#         if n == 2:
#             return j
#         j += 1
# print(second_index("sims", " "))

# 14
# def frequency_sort(items):                      # Cортировка объектов по их частоте в строке
#     dict ={item : items.count(item) for item in items}
#     list_dict = list(dict.items())
#     list_dict.sort(key=lambda i: i[1], reverse = True)
#     dict_2 = {i[0] : i[1] for i in list_dict}
#     return [key for key in dict_2.keys() for i in range(dict_2[key])]
# print(frequency_sort([4,6,2,2,2,6,4,4,4]))

# 15
# def safe_pawns(pawns):                                                                  # Что-то на Шахматском
#     dict_l = {'a':'b', 'b':'a', 'c':'b', 'd':'c', 'e':'d', 'f':'e', 'g':'f', 'h':'g'}
#     dict_r = { 'a':'b', 'b':'c', 'c':'d', 'd':'e', 'e':'f', 'f':'g', 'g':'h', 'h':'g'}
#     list = {(dict_l[i[0]], str(int(i[1]) + 1)) for i in pawns } | {(dict_r[i[0]], str(int(i[1]) + 1)) for i in pawns }
#     list = tuple(list)
#     result = {"".join(list[j]) for j in range(len(list))} & pawns
#     return len(result)
# print(safe_pawns({"a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"}))

# 16
# def sun_angle(time):
#     time = time.split(":")
#     time = int(time[0]) * 60 + int(time[1])
#     if 360 <= time <= 1080:
#         time -= 360
#         return time*0.25
#     else:
#         return "I don't see the sun!"
# print(sun_angle("18:00"))

# 17
# def split_list(items):
#     if len(items) % 2 == 0:
#         result = [items[:round(len(items) / 2)], items[round(len(items) / 2) :]]
#     else:
#         result = [items[:int(len(items) / 2) +1], items[int(len(items) / 2) +1 :]]
#     return result
# print(split_list([1,2,3,4,5,6,7,8,9]))
# 18
# def all_the_same(elements):
#     if len(elements) == 0:
#         return True
#     else:
#         return elements.count(elements[0]) == len(elements)
# print(all_the_same([]))

# 19
# def date_time(time):
#     dictanory = {"01": 'January', "02": 'February', "03": 'March', "04": 'April', "05": 'May', "06": 'June', \
#                  "07": 'July', "08": 'August', "09": 'September', "10": 'October', "11": 'November', "12": 'December', }
#     time = time.split(" ")
#     time_date = time[0].split(".")
#     time = time[1].split(":")
#     result = str(int(time_date[0])) +" "+ dictanory[time_date[1]] + ' {} year {} hours {} minutes'.format(time_date[2], int(time[0]), int(time[1]))
#     if int(time[0]) == 1:
#         result = result.replace("hours", 'hour')
#     if int(time[1]) == 1:
#         result = result.replace("minutes", "minute")
#     return result
# print(date_time("01.02.2000 01:01"))

# 20
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
# print(morse_decoder("###    ... --- -- .   - . -..- - -.- . -.-- . .-. .-. --- .-


# Остров Пройден!!!
