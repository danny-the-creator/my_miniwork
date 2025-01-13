# 1
# def checkio(values):
#     values = {abs(i):i for i in values }
#     return [ values[i] for i in sorted(values)]
# print(checkio([-20, -5, 10, 15]))

# 2
# def goes_after(word, first, second):
#     list = []
#     for i in word:
#         if i not in set(list):
#             list.append(i)
#     return bool("".join(list).count(first + second))
# print(goes_after("transport","t","r"))

# 3
# def time_converter(time):
#     time = time.split(':')
#     if int(time[0]) < 12:
#         return f"{str(int(time[0]))}:{time[1]} a.m.".replace("0:", "12:").replace("112:", "10:")    # Отстаньте
#     else:
#         return f"{str(int(time[0])-12)}:{time[1]} p.m.".replace("0:", "12:").replace("112:", "10:") # Отстаньте
# print(time_converter("22:30"))

# 4
# def sum_by_types(items):
#     numbers = [i for i in items if type(i) == int]
#     longword = [j for j in items if type(j) == str]
#     return ("".join(longword), sum(numbers))
# print(sum_by_types([12, 9, 45, 0]))

# 5
# def translate(text):
#     vowels, n = {'a', 'e', 'i', 'o', 'u', 'y', ' ', ''}, 0
#     text = [i for i in text]
#     for i in text:
#         if i not in vowels:
#             text[n+1] = ''
#         n += 1
#     text = "".join(text)
#     for j in vowels - {' ', ''}:
#         text = "".join(text).replace(j*3, j)
#     return text
# print(translate('hoooowe yyyooouuu duoooiiine'))

# 6
# def checkio(line1, line2):
#     result = list(set(line1.split(",")) & set(line2.split(",")))
#     result.sort()
#     return ",".join(result)
# print(checkio('one,two,three', 'four,five,one,two,six,three'))

# 7
# def follow(instructions):
#     fb = rl = 0
#     for i in instructions:
#         if i == 'f':
#             fb += 1
#         elif i == 'b':
#             fb -= 1
#         elif i == 'r':
#             rl += 1
#         elif i =='l':
#             rl -= 1
#     return [rl, fb]
# print(follow(""))

# 8
# import re
# def check_pangram(text):
#     letters = ['a','b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     letters_in_text = [i for i in letters if bool(re.search(i, text.lower())) == True]
#     return letters == letters_in_text
# print(check_pangram("ABCDEF."))

# 9
# def checkio(text):
#     max_quantity = 0
#     letters = 'abcdefghijklmnopqrstuvwxyz'
#     for letter in letters[::-1]:
#         quantity = text.lower().count(letter)
#         if quantity >= max_quantity:
#             max_quantity = quantity
#             result = letter
#     return result
# print(checkio(''))

# 10
# def letter_queue(commands):
#     text = ''
#     for command in commands:
#         if command == 'POP':
#             text = text[1:]
#         elif command.split(' ')[0] == 'PUSH':
#             text += command.split(' ')[1]
#     return text
# print(letter_queue(['PUSH A', 'POP', 'POP', 'PUSH Z', 'PUSH D', 'PUSH O', 'POP', 'PUSH T']))

# 11
# def from_camel_case(name):
#     list = []
#     for letter in name:
#         if letter == letter.upper():
#             list.append('_')
#             letter = letter.lower()
#         list.append(letter)
#     return ''.join(list[1:])
#
# print(from_camel_case("MyFunctionName"))


# 11.5
# def to_camel_case(name):
#     result =[]
#     name = name.split('_')
#     for i in name:
#         result.append(i.capitalize())
#     print(result)
#     return ''.join(result)
# print(to_camel_case("i_phone"))

#12
# import re
# def checkio(text, word):
#     def space_deleter(text):
#         """Cоздаёт список из введённого предложения, разбивая его по пробелам, но игнорируя множественные пробелы"""
#         split = text.split(' ')
#         return "".join([i for i in split if len(i) != 0])
#     text = space_deleter(text).lower()
#     text = text.split('\n')
#     for string in text:
#         if bool(re.search(word, string)) == True:
#             column_start, column_end = re.search(word, string).span()
#             row_start = row_end = text.index(string)
#             return [row_start+1, column_start+1, row_end+1, column_end]   # Перевод координат из программерского в нормальный (Отсчёт должен начинаться не с 0, а с 1)
#
#     text = [[i for i in j] for j in text]                                       # Уравнивает длинну всех строк путём добавления '&'
#     while min(*[len(i) for i in text]) != max(*[len(i) for i in text]):
#         for i in text:
#             if len(i) != max(*[len(i) for i in text]):
#                 i += '&'
#     text = [''.join(i) for i in text]
#
#     text = [''.join([j[i] for j in text]) for i in range(len(text[0]))]     # выводит текст написанный по столбцам (не пытайся разобраться)
#     for string in text:
#         if bool(re.search(word, string)) == True:
#             row_start, row_end = re.search(word, string).span()
#             column_start = column_end = text.index(string)
#             return [row_start + 1, column_start + 1, row_end, column_end+1]  # Перевод координат из программерского в нормальный (Отсчёт должен начинаться не с 0, а с 1)

# 13
# def find_message(message):
#     return ''.join([i for i in message if i in 'QWERTYUIOPASDFGHJKLZXCVBNM'])
# print(find_message('How are you? Eh, ok. Low or Lower? Ohhh.'))

#14
# def caps_lock(text):
#     result = []
#     CapsLock_control = -10
#     for letter in text:
#         if letter == 'a':
#             CapsLock_control *= -1
#             continue
#         if CapsLock_control > 0:
#             letter = letter.upper()
#         result.append(letter)
#     return ''.join(result)
#
# print(caps_lock("Aloha from Hawaii") == "Aloh FROM HwII")

#15
# def yaml(a):
#     object = {}
#     a = a.replace(' ', '')
#     commands = a.split('\n')
#     commands = [command for command in commands if len(command) != 0]
#     for command in commands:
#         key, value = command.split(':')
#         try:
#             value = int(value)
#         except:
#             pass
#         object[key] = value
#     return sorted(object)
# print(yaml("name: Alex\nage: 12"))

#16
# def yaml(a):
#     object = {}
#     a = a.replace(' ', '')
#     commands = a.split('\n')
#     commands = [command for command in commands if len(command) != 0]
#     for command in commands:
#         try:
#             key, value = command.split(':')
#         except:
#             object[command] = None
#             return
#         try:
#             value = int(value)
#         except:
#             value = value.replace(' ', '')
#             if value.lower() == 'True':
#                 value = True
#             elif value.lower() == 'False':
#                 value = False
#         try:
#             value.replace('\'', '').replace('"', '')
#         except:
#             pass
#
#         object[key] = value
#     object = {i : object[i] for i in sorted(object.keys(), key= lambda x: len(x))}
#     return object
#
# print(yaml("name: Alex Fox\nage: 12\n\nclass: 12b"))

#17
# def turn90(square):
#     '''Не знаю как я это сделал, но функция действительно разворачивает квадрат на 90 градусов'''
#     new_square = []
#     for i in range(len(square)):
#         line = square[i]
#         new_square.append([])
#         for j in range(len(line)):
#             new_square[i].append(square[(j+1)*(-1)][i])
#     return new_square
# def recall_password(grille, password):
#     result = []
#     for n in range(4):
#         # for i in range(len(grille)):
#         #     line = grille[i]
#         #     for j in range(len(line)):
#         #         if grille[i][j] == 'X':
#         #             result.append(password[i][j])
#         square = [password[i][j] for i in range(len(grille)) for j in range(len(grille[i])) if grille[i][j] =='X']          # аналог верхнего кода
#         result.extend(square)
#         grille = turn90(square=grille)
#     return ''.join(result)
# print(recall_password(['X...', '..X.', 'X..X', '....'],
#  ['itdf', 'gdce', 'aton', 'qrdi']))
