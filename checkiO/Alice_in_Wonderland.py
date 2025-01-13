# 1
# from datetime import date
# def friday(day_):
#     day, month, year = day_.split('.')
#     time = date(day=int(day), month=int(month), year=int(year))
#     current_weekday = time.isoweekday()
#
#     if (5 - current_weekday) < 0:
#         return (5 - current_weekday) + 7
#     return (5 - current_weekday)
# print(friday("02.01.1999"))

# 2
# def create_zigzag(rows, cols, start=1):
#     result = []
#     for row in range(rows):
#         result.append([])
#         for colon in range(cols):
#             result[row].append(start)
#             start += 1
#     result = [i[::-1] if result.index(i) % 2 != 0 else i for i in result]
#     return result
#
# print(create_zigzag(3, 5) == [[1,2,3,4,5],
#                               [10,9,8,7,6],
#                               [11,12,13,14,15]])

# 3 !!!
# def middle(text):                           # Возвращает середину строки (Работает с помощью РЕКУРСИИ!!!) Это успех!!!
#     if len(text) in [0, 1, 2]:
#         return text
#     return middle(text[1:-1])

# 4
# def flood_area(diagram):                        # Я сам не до конца понимаю как она работает
#
#     '''Сначала каждому элементу выдаёт координаты и сортирует по высоте, потом в этом порядке (по убыванию высоты)
#      функция итерируется по всем элементам с данной высотой, высчитывает объём воды и добавляет его к результату,
#      также находит своё положение в этом списке и прибавляется к другому объёму если эти объёмы воды сливаются вместе'''        # Как-то так...
#     hight = 0
#     coordinates = []
#     for i in range(len(diagram)):
#         shape = diagram[i]
#         if shape == '\\':
#             hight -= 1
#             coordinates.append((shape, i, hight))
#         elif shape == '/':
#             coordinates.append((shape, i, hight))
#             hight += 1
#         elif shape == '_':
#             coordinates.append((shape, i, hight))
#     coordinates.sort(key=lambda x: x[2], reverse=-1)           # ???
#     # return coordinates
#     top_hight = coordinates[0][2]
#     bottom_hight = coordinates[-1][2]
#     result = []
#     if True:                        # for hight in range(top_hight, bottom_hight-1, -1):
#         waterstart = None
#         for shape in coordinates:
#             hight = shape[2]
#             # if shape[2] != hight:
#             #     continue
#             if shape[0] == '\\':
#                 waterstart = shape
#             if shape[0] == '/' and waterstart != None:
#                 water_level = {'volume' : shape[1]-waterstart[1],
#                                'size' : (waterstart[1], shape[1]),
#                                'hight' : hight}
#
#                 waterstart = None                       # ??
#
#                 if hight == top_hight:
#                     result.append(water_level)
#                     continue
#                 found = False
#                 for level in result:
#                     if level['size'][0] < water_level['size'][0] < level['size'][1]:
#                         level['volume'] += water_level['volume']
#                         level['hight'] = hight
#                         found = True
#                         break
#                     elif level['size'][0] > water_level['size'][0]:
#                         result = result[:result.index(level)] + [water_level] + result[result.index(level):]
#                         found = True
#                         break
#                 if found == False:
#                     result.append(water_level)
#
#     if result == []:
#         return result
#     else:
#         return [i['volume'] for i in result if i['volume'] > 0]
#
# input = input()
# print(flood_area(input))


# 5     !!! Не моя программа (слишком скучная)
# def diff1(t,s):
# 	r=0
# 	for i in range(len(t)):
# 		if t[i]!=s[i]: r+=1
# 		if r>1: return False
# 	return True

# def checkio(numbers):
# 	numbers=[str(e) for e in numbers]
# 	f=numbers.pop(0)
# 	l=numbers.pop()
# 	if f==l: return [int(f),int(l)]
# 	h={f:None}
# 	q=[(f,0)]
# 	while len(q)>0:
# 		x,y=q.pop(0)
# 		if diff1(x,l):
# 			q.append((l,y+1))
# 			h[l]=x
# 			break
# 		for e in numbers:
# 			if e not in h and diff1(x,e):
# 				q.append((e,y+1))
# 				h[e]=x
# 	if len(q)==0: return []
# 	a=[l]
# 	x=l
# 	while h[x]:
# 		a.append(h[x])
# 		x=h[x]
# 	return [int(e) for e in reversed(a)]

# 6
# def checkio(first, second):
#     first = str(bin(first))[2:]
#     second = str(bin(second))[2:]
#     result_and = []
#     result_or  = []
#     result_xor = []
#     for element in range(len(first)):
#         i = int(first[element])
#         result_and.append([])
#         result_or.append([])
#         result_xor.append([])
#         for j in second:
#             j = int(j)
#             result_and[element].append(str(j and i))
#             result_or[element].append(str(j or i))
#             result_xor[element].append(str(int(j != i)))
#
#     return sum([int(''.join(i), 2) for i in result_and]) + sum([int(''.join(i), 2) for i in result_or]) + sum([int(''.join(i), 2) for i in result_xor])
#
# print(checkio(7, 2))

# 7         !!! Поиск в ширину !!! (моя собственная программа)
def checkio(cells):
    '''Функция показывает, сколько шагов по графама она сделала, чтобы найти нужное значение.

    В данном конкретном примере: находим минимальное количество шагов за которое коняшка в шахматач дойдёт из клетки а в клетку b'''
    first_position, last_position = cells.split('-')
    vertical = ['1','2','3','4','5','6','7','8']
    horizontal = ['a','b','c','d','e','f','g','h']
    search_queue = []
    current_queue = [first_position]
    searched = []
    result = 0
    while current_queue != []:
        position = current_queue.pop(0)
        if position == last_position:
            break
        if position not in searched:
            new_positions =  [horizontal[horizontal.index(position[0])+a]+vertical[vertical.index(position[1])+b] for a in [-2, 2] for b in [-1, 1] if 0 <= (horizontal.index(position[0])+a) < 8 and 0 <= (vertical.index(position[1])+b) < 8 ]
            new_positions += [horizontal[horizontal.index(position[0])+b]+vertical[vertical.index(position[1])+a] for a in [-2, 2] for b in [-1, 1] if 0 <= (horizontal.index(position[0])+b) < 8 and 0 <= (vertical.index(position[1])+a) < 8 ]
            #                                 # не пытайся понять, как работают эти генераторы списков, главное, что они возвращают все возможные ходы конём исходя из его позиции

            search_queue.extend(new_positions)
            searched.append(position)
        if current_queue == []:
            result+=1
            current_queue = search_queue
            search_queue = []

    return result

# print(checkio('d5-b1'))

# 8
# def int_palindrome(number, B):
#     alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-+=abcdefghijklmnopqrstuvwxyz[]{}цукенгшщзхъфывапролджэячсмитьбю."
#     res = ""
#     while number > 0:
#         number, m = divmod(number, B)
#         res += alphabet[m]
#     number = res[::-1]
#     return number == number[::-1]
#
# print(int_palindrome(455,2))

#9
# def tree_walker(tree, target):
#     result = []                     # раз костыль
#     if tree == target:              # два костыль
#         return 1
#     if type(tree) == dict:          # три костыль
#         tree = list(tree.values())
#     def get_leafs(tree):
#         nonlocal result
#         for branch in tree:
#             if branch == target:
#                 result.append(branch)
#             elif type(branch) in [list, dict]:
#                 if type(branch) == dict:
#                     branch = list(branch.values())
#                 get_leafs(branch)
#
#     get_leafs(tree)
#     return result.count(target)     # опять костыль
#           # A некостыльный вариант тест не прошёл), а он работал )
# print(tree_walker({"one":[1,2],"two":[{"1":"one","2":"two"},[1,2],"1","one"]},[1,2]))

#10,11         # ! NOT MY Solution !
# def convert(value):                                         # return converted
#     transform = {'"null"': 'null', '': None, 'null': None,  # value
#                  'true': True, 'false': False}              #
#     if value in transform:
#         return transform[value]
#     value = value.replace('\\', '').replace('\"', '"')
#     if value[0] == value[-1] == '"':
#         value = value[1:-1]
#     return int(value) if value.isdigit() else value
#
# def remove_comment(text):                                   # remove comment
#     quoted, data = False, ''                                # from line
#     for char in text:                                       #
#         if char == '"':
#             quoted = not quoted
#         if char == '#' and not quoted:
#             return data
#         data += char
#     return data
#
# def get_yaml(text):                                         # recursively get yaml
#     index = lambda x: len(x) - len(x.lstrip())              # block indent
#     ix = index(text[0])                                     #
#     (delimeter, result) = ('-', []) if '-' in text[0] else (':', {}) # type of block
#     while text:                                             # let's go through the block
#         line = text.pop(0)                                  # get line
#         key, value = line.split(delimeter)                  # get key and value
#         key, value = key.strip(), convert(value.strip())    # if list then key = ''
#         if line.strip()[-1] == delimeter and text and index(text[0]) != ix:
#             subtext = []                                    # if find sub-block, go recursively through one
#             while text and index(text[0]) != ix:            # get subblock text
#                 subtext.append(text.pop(0))                 #
#             value = get_yaml(subtext)                       # recursion
#         if delimeter == ':':                                #
#             result.update({key: value})                     # add value to result
#         else:                                               #
#             result.append(value)                            #
#     return result                                           #
#
# def yaml(a):
#     value = [remove_comment(line) for line in a.split('\n') if line and line[0] != '#']
#     return get_yaml(value)