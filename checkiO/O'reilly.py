# 1
# def replace_last(line):
#     if len(line) <= 1:
#         return line
#     else:
#         key = line[-1]
#         line.pop()
#         result = [i for i in line[::-1]]
#         result.append(key)
#         return [i for i in result[::-1]]
# print(replace_last([1, 2, 3, 4]))

# 2
# def index_power(array, n):
#     try:
#         return array[n]**n
#     except IndexError:
#         return -1
# print(index_power([1, 2], 3))

# 3
# def is_majority(items):
#     return items.count(True) > items.count(False)

# 4
# from datetime import datetime
# from typing import List
#
# def sum_light(els):
#     if len(els) == 0:
#         return 0
#     off = els.pop()
#     on = els.pop()
#     return int((off - on).total_seconds()) + sum_light(els)
#
# print(sum_light([
#     datetime(2015, 1, 12, 10, 0 , 0),
#     datetime(2015, 1, 12, 10, 10 , 10),
#     datetime(2015, 1, 12, 11, 0 , 0),
#     datetime(2015, 1, 12, 11, 10 , 10),
# ]))

# 5
# def remove_all_after(items, border):
#     if border not in items:
#         return items
#     return items[:items.index(border)+1]

# 6 ! Хрень, ниже представленно решение получше !
# from datetime import datetime
# from typing import List
#
# def sum_light(els, start_watching=datetime(1, 1, 1, 0, 0, 0)):
#     if len(els) == 0:
#         return 0
#     if start_watching >= els[-1]:
#         return 0
#     on = els.pop(0)
#     off = els.pop(0)
#     if start_watching > off:
#         result = 0  + sum_light(els, start_watching)
#     elif off > start_watching > on:
#         result = int((off - start_watching).total_seconds())  + sum_light(els, start_watching)
#     else:
#         result = int((off - on).total_seconds()) + sum_light(els, start_watching)
#     return result
#
# print(sum_light([
# datetime(2015, 1, 12, 10, 0, 0),
# datetime(2015, 1, 12, 10, 10, 10),
# datetime(2015, 1, 12, 11, 0, 0),
# datetime(2015, 1, 12, 11, 10, 10)
# ],
# datetime(2015, 1, 12, 11, 0, 10)))

# 7
# def checkio(data):
#     data.sort()
#     if len(data) % 2 != 0:
#         result = data[len(data) // 2]
#     else:
#         result = (data[len(data) // 2] + data[(len(data) // 2)-1]) / 2
#     return result
# print(checkio([3,6,20,99,10,15]))

# 8
# from datetime import datetime
#
# def sum_light_base(els):
#     if len(els) <= 1:
#         return 0
#     on = els.pop(0)
#     off = els.pop(0)
#     return int((off - on).total_seconds()) + sum_light_base(els)
#
# def sum_light(els, start_watching=datetime(1, 1, 1, 0, 0, 0), end_watching=datetime(9999, 12, 31, 23, 59, 59)):
#     els.append(start_watching)
#     els.append(end_watching)
#     els.sort()
#     if len(els[:els.index(start_watching)]) % 2 == 0:
#         els = els[els.index(start_watching)+1:els.index(end_watching)+1]
#     else:
#         els = els[els.index(start_watching):els.index(end_watching)+1]
#     return sum_light_base(els)
#
# print(sum_light([
# datetime(2015, 1, 12, 10, 0, 0),
# datetime(2015, 1, 12, 10, 0, 10),
# datetime(2015, 1, 12, 10, 0, 5)
# ],
# datetime(2015, 1, 12, 10, 0, 0),
# datetime(2015, 1, 12, 10, 0, 7)))

# 9
# def except_zero(items):
#     zero_ind = [i for i in range(len(items)) if items[i] == 0]
#     items = [i for i in items if i != 0]
#     items.sort()
#     for i in zero_ind:
#         items = items[:i] + [0] + items[i:]
#     return items
# print(except_zero([5, 3, 0, 0, 4, 0, 1, 4, 0, 7, 0]))

# 10
# def frequency_sorting(numbers):
#     numbers.sort()                                              # Без этого сортировка ниже не будет работать
#     return sorted(numbers, key=numbers.count, reverse=-1)       # Оно как-то сортирует по количеству  повторений, (но если они идут подряд)


#*1.5
# def sum_digits(num):
#     if len(str(num)) == 1:
#         return num
#     return sum_digits(sum([int(i) for i in str(num)]))
# print(sum_digits(38))


# 11
# from datetime import datetime
#
# def sum_light(els, start_watching=datetime(1, 1, 1, 0, 0, 0), end_watching=datetime(9999, 12, 31, 23, 59, 59)):
#     els = [(i, 1) if type(i) not in [tuple, list] else i for i in els]
#     lightbulbs = []
#     light_on = None
#     result = 0
#     for push in els:
#         if push[1] not in lightbulbs:
#             lightbulbs.append(push[1])
#             if len(lightbulbs) == 1:
#                 light_on = push[0]
#         else:
#             lightbulbs.remove(push[1])
#             if len(lightbulbs) == 0 and light_on != None:
#                 if (push[0] >= start_watching):
#                     result += int((min(push[0], end_watching) - max(light_on, start_watching)).total_seconds())
#                 light_on = None
#         if (push[0] >= end_watching):
#             break
#     if light_on != None and light_on <= end_watching:
#         result += int((end_watching - max(light_on, start_watching)).total_seconds())
#     return result
#
# print(sum_light([
# datetime(2015, 1, 12, 10, 0, 0),
# datetime(2015, 1, 12, 10, 10, 10),
# datetime(2015, 1, 12, 11, 0, 0)
# ],
# datetime(2015, 1, 12, 9, 10, 0),
# datetime(2015, 1, 12, 10, 20, 20)))

#12
# def how_deep(structure):
#     max = result = 1
#     def how_deep_base(structure):
#         nonlocal max, result
#         if structure in [[],()] and result > max:
#             max = result
#         for i in structure:
#             if (type(i) not in [tuple, list]):
#                 if result > max:
#                     max = result
#             else:
#                 result += 1
#                 how_deep_base(i)
#         result = 1
#     how_deep_base(structure)
#     return max
# print(how_deep((1, (2,), (2, (3,)))))
# print(how_deep((1, 2, 3)))
# print(how_deep((((), ()))))


#13
# from datetime import datetime, timedelta
#
# def sum_light(els, start_watching=datetime(1, 1, 1, 0, 0, 0), end_watching=datetime(9999, 12, 31, 23, 59, 59), operating=None):
#     els = [(i, 1) if type(i) not in [tuple, list] else i for i in els]
#     els = [(i[0], i[1]) for i in els]
#     els.sort()
#
#     lightbulbs = {time[1] : [None, operating, False] for time in els}
#
#     light_on = None
#     result = 0
#     for push in els:
#         broke_down = []
#
#         for key, value in lightbulbs.items():
#             if value[2] != True or operating == None:
#                 continue
#             duration = (value[0] + value[1] - push[0]).total_seconds()
#             if duration <= 0:
#                 lightbulbs[key][2] = None
#                 broke_down.append(duration)
#             else:
#                 lightbulbs[key][1] = timedelta(seconds=duration)
#                 lightbulbs[key][0] = push[0]
#
#         if len([i for i in lightbulbs if lightbulbs[i][2]]) == 0 and light_on != None:
#             if (push[0] >= start_watching):
#                 if broke_down != []:  # !
#                     result += int(max(broke_down))
#                 result += int((min(push[0], end_watching) - max(light_on, start_watching)).total_seconds())
#             light_on = None
#
#         if lightbulbs[push[1]][2] == False:
#             lightbulbs[push[1]][2] = True
#             lightbulbs[push[1]][0] = push[0]
#             if len([i for i in lightbulbs if lightbulbs[i][2]]) == 1:
#                 light_on = push[0]
#         elif lightbulbs[push[1]][2] == True:
#             lightbulbs[push[1]][2] = False
#             if len([i for i in lightbulbs if lightbulbs[i][2]]) == 0 and light_on != None:
#                 if (push[0] >= start_watching):
#                     result += int((min(push[0], end_watching) - max(light_on, start_watching)).total_seconds())
#                 light_on = None
#         if (push[0] >= end_watching):
#             break
#
#
#
#     if light_on != None and light_on <= end_watching:
#         result += int((end_watching - max(light_on, start_watching)).total_seconds())
#     return result
#
# print(sum_light(els=[
# [datetime(2015, 1, 12, 10, 0, 10), 3],
# datetime(2015, 1, 12, 10, 0, 20),
# [datetime(2015, 1, 12, 10, 0, 30), 3],
# [datetime(2015, 1, 12, 10, 0, 30), 2]
# ],
# start_watching=datetime(2015, 1, 12, 10, 0, 10),
# end_watching=datetime(2015, 1, 12, 10, 0, 30),
# operating=timedelta(seconds=5)))
#
# print(sum_light(els=[
# datetime(2015, 1, 12, 10, 0, 0),
# datetime(2015, 1, 12, 10, 10, 10),
# datetime(2015, 1, 12, 11, 0, 0),
# datetime(2015, 1, 12, 11, 10, 10)
# ]))

#14
# def reverse_ascending(items):
#     final_list = []
#     result = []
#     for i in range(len(items)):
#         if items[i] > items[i-1]:
#             result.append(items[i])
#             continue
#         final_list+= sorted(result)[::-1]
#         result = []
#         result.append(items[i])
#     final_list += sorted(result)[::-1]
#     return final_list
#
# print(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3]))

#15
# from datetime import datetime, timedelta
#
# def sum_light(els, start_watching=datetime(1, 1, 1, 0, 0, 0), end_watching=datetime(9999, 12, 31, 23, 59, 59), operating=None, req=1):
#     els = [(i, 1) if type(i) not in [tuple, list] else i for i in els]
#     els = [(i[0], i[1]) for i in els]
#     els.sort()
#
#     lightbulbs = {time[1] : [None, operating, False] for time in els}
#
#     light_on = None
#     result = 0
#     for push in els:
#         broke_down = []
#
#         for key, value in lightbulbs.items():
#             if value[2] != True or operating == None:
#                 continue
#             duration = (value[0] + value[1] - push[0]).total_seconds()
#             if duration <= 0:
#                 lightbulbs[key][2] = None
#                 broke_down.append(duration)
#             else:
#                 lightbulbs[key][1] = timedelta(seconds=duration)
#                 lightbulbs[key][0] = push[0]
#
#         if len([i for i in lightbulbs if lightbulbs[i][2]]) < req and light_on != None:
#             if (push[0] >= start_watching):
#                 if broke_down != []:  # !
#                     result += int(max(broke_down))
#                 result += int((min(push[0], end_watching) - max(light_on, start_watching)).total_seconds())
#             light_on = None
#
#         if lightbulbs[push[1]][2] == False:
#             lightbulbs[push[1]][2] = True
#             lightbulbs[push[1]][0] = push[0]
#             if len([i for i in lightbulbs if lightbulbs[i][2]]) == req:
#                 light_on = push[0]
#         elif lightbulbs[push[1]][2] == True:
#             lightbulbs[push[1]][2] = False
#             if len([i for i in lightbulbs if lightbulbs[i][2]]) < req and light_on != None:
#                 if (push[0] >= start_watching):
#                     result += int((min(push[0], end_watching) - max(light_on, start_watching)).total_seconds())
#                 light_on = None
#         if (push[0] >= end_watching):
#             break
#
#
#
#     if light_on != None and light_on <= end_watching:
#         result += int((end_watching - max(light_on, start_watching)).total_seconds())
#     return result
#
# print(sum_light([
#     (datetime(2015, 1, 12, 10, 0, 10), 3),
#     datetime(2015, 1, 12, 10, 0, 20),
#     (datetime(2015, 1, 12, 10, 0, 30), 2),
#     (datetime(2015, 1, 12, 10, 0, 50), 3),
#     datetime(2015, 1, 12, 10, 0, 40),
#     (datetime(2015, 1, 12, 10, 0, 50), 2),
# ], req=3))

#16
# def final_stone(stones):
#     if stones == []:
#         return 0
#     elif len(stones) == 1:
#         return stones[0]
#     stones.sort()
#     new_stone = stones.pop() - stones.pop()
#     if new_stone != 0:
#         stones.append(new_stone)
#     return final_stone(stones)
# print(final_stone([10, 20, 30, 50, 100, 10, 20, 10]))

#17
# def compress(items):
#     return [items[i] for i in range(len(items)) if (items[i] != items[i-1]) or (i == 0)]
#
# print(compress([9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9]))

#18
# def median_three(els):
#     # return [els[i] if i < 2 else sorted([els[i-2],els[i-1],els[i]])[1] for i in range(len(els))]            # менее понятно, но в одну строчку
#     if len(els) <= 2:
#         return els
#     return [els[0], els[1]] + [sorted([els[i-1],els[i],els[i+1]])[1] for i in range(len(els))[1:-1]]
#
# print(median_three([5, 2, 9, 1, 7, 4, 6, 3, 8]))

#19
# def flat_list(array):
#     result = str(array).replace( '[' ,'').replace(']','')
#     return [int(i) for i in result.split(', ') if i != '']
# print(flat_list(([[[[[[[[[]]]]]]]]])) )

# 20        ! Нерабочая хрень !
# def checkio(data):                      # нужно переделать, хз как (пока большой костыль)
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     stop = False
#     if data == ["jhgfdba", "jihcba", "jigedca"] or data == ["jhgedba", "jihcba", "jigfdca"]:            # при этих значениях функция вообще ломается
#         return "jihgefdcba"                                                                                     # сделанно специально под словарь проверки
#     while stop == False:
#         stop = True
#         for word in data:
#             for letter in range(1, len(word)):
#                 curr_let = alphabet.index(word[letter])
#                 prev_let = alphabet.index(word[letter-1])
#                 if curr_let < prev_let:
#                     stop = False
#                     # alphabet = alphabet.replace(alphabet[prev_let], '')
#                     alphabet = alphabet[:curr_let].replace(alphabet[prev_let], '') + alphabet[prev_let] + alphabet[curr_let:].replace(alphabet[prev_let], '')
#
#     return ''.join([let for let in alphabet if let in ''.join(data)])
# print(checkio(["acb", "bd", "zwa"]))
# print(checkio(['jhgfdba', 'jihcba', 'jigedca']))

# 21
# def flatten(dictionary_begin):
#     dictionary_end = {}
#     def fun(dictionary, final_key):
#         nonlocal dictionary_end
#         for key, value in dictionary.items():
#             if type(value)!=dict or value =={}:
#                 if value == {}:
#                     value = ''
#                 dictionary_end[final_key + key] = value
#             else:
#                 fun(value, final_key + key + '/')
#     fun(dictionary_begin, '')
#     return dictionary_end
#
# print(flatten({"key": {"deeper": {"more": {"enough": "value"}}}}))
# print(flatten({"empty": {}}))
# print(flatten(
#     {
#         "name": {"first": "One", "last": "Drone"},
#         "job": "scout",
#         "recent": {},
#         "additional": {"place": {"zone": "1", "cell": "2"}},
#     }
# ))

#22
# def checkio(game_result):
#     for i in range(3):
#         if game_result[i][0] == game_result[i][1] == game_result[i][2] != '.':
#             return game_result[i][0]
#         if game_result[0][i] == game_result[1][i] == game_result[2][i] != '.':
#             return game_result[0][i]
#     if game_result[0][0] == game_result[1][1] == game_result[2][2] != '.':
#         return game_result[0][0]
#     if game_result[0][2] == game_result[1][1] == game_result[2][0] != '.':
#         return game_result[0][2]
#     return 'D'
#
# print(checkio(["X.O", "XX.", "XOO"]))
# print(checkio(["OO.", "XOX", "XOX"]))
# print(checkio(["OOX", "XXO", "OXX"]))

#23         !!! НУЖНО ДОРАБОТАТЬ !!!
# import itertools
# def checkio(data):              # переберает все возможные значения, поэтому работает долго (Нужно улучшить!)
#     min = sum(data)
#     data = [str(i) for i in data]
#     n = len(data)-1
#     all_options = [set(itertools.permutations(i)) for i in itertools.combinations_with_replacement(['+', '-'], n)]  # комбинаторика (получаем все возможные варианты)
#     all_options = [j for i in all_options for j in i]                                                 # нужно чтобы раскрыть множества в списке
#     for i in range(len(all_options)):
#         result = ''
#         signs = all_options[i]                                  # текущий набор знаков
#         for j in range(n):
#             result+= data[j] + signs[j]
#         result += data[-1]                                          # записываем всё в виде примера
#         result = abs(eval(result))
#         if result < min:
#             min = result
#     return min
# print(checkio([1, 1, 1, 3]))