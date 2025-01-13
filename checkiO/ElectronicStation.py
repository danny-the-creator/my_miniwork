# 1
# def words_order(text, words):           # Проверка на порядок слов в тексте (совпадает-ли он с порядком слов в списке)
#     text = text.split(" ")
#     result = [i for i in text if i in set(words)]
#     list = []
#     for i in result:
#         if i not in set(list):
#             list.append(i)
#     return list == words
# print(words_order("", ["world"]))

# def sort_by_ext(files):
#     extensions = {}
#     for file in files:
#         file_split = file.split(".")
#         if len(file_split) < 2 or (len(file_split) == 2 and file_split[0] == ''):
#             if file_split[0] == '':
#                 file_split[-1] = '.'+file_split[-1]
#             file_split = [file_split[-1], ""]
#         elif file_split[-1] == '':
#             file_split[-2] += '.'
#         if extensions.get(file_split[-1]) == None:
#             extensions[file_split[-1]] = [".".join(file_split[:-1])]
#             continue
#         extensions[file_split[-1]].append(".".join(file_split[:-1]))
#     for extension in sorted(extensions):
#         extensions[extension].sort()
#     # generates a sorted list with the priority over extensions (keys) if the file had no extension
#                                       we return just the name without a point in the end, unless the name had one
#     return [(lambda v, k:'.'.join((v, k)) if k != '' else v)(v,k) for k in sorted(extensions) for v in sorted(extensions[k])]
#
# print( sort_by_ext(["1.cad", "1.bat", ".aa", ".bat"]))
# print(sort_by_ext(["1.cad", "1.bat", "1.aa", "1.aa.doc"]))
# print(sort_by_ext(["1.cad", "1.bat", "1.aa", ".aa.doc"]))
# print(sort_by_ext(['1.cad', '1.', '1.aa']))

#3
# def checkio(number):
#     result = 1
#     for digit in str(number).replace('0',''):
#         result *= int(digit)
#     return result

#4, 5, 6, 7, 8
import re
# def is_acceptable_password(password):
#     return len(set(password)) > 2 and not re.search('password', password.lower()) and (len(password) > 9 or
#                         (len(password) > 6 and bool(re.search(r'\d', password)) and bool(re.search(r'\D', password))))
#
# print(is_acceptable_password('454545457777'))

# 9
# def is_all_upper(text):
#     return text == text.upper() and text != text.lower()

#10
# def is_ascending(items):
#     # your code here
#     return len(set(items)) == len(items) and items == sorted(items)

#11
# def distribute_blood(blood_avail, blood_needs):
#     distribution = {'A': {'A': 0, 'B': 0, 'AB': 0, 'O': 0},
#                     'B': {'A': 0, 'B': 0, 'AB': 0, 'O': 0},
#                     'AB': {'A': 0, 'B': 0, 'AB': 0, 'O': 0},
#                     'O': {'A': 0, 'B': 0, 'AB': 0, 'O': 0}}
#     blood_avail['O'] -= blood_needs['O']
#     distribution['O']['O'] += blood_needs['O']
#
#     blood_avail['A'] -= blood_needs['A']
#     if blood_avail['A'] < 0:
#         blood_avail['O'] += blood_avail['A']
#         distribution['A']['A'] += blood_avail['A']
#         distribution['O']['A'] -= blood_avail['A']
#         blood_avail['A'] = 0
#     distribution['A']['A'] += blood_needs['A']
#
#     blood_avail['B'] -= blood_needs['B']
#     if blood_avail['B'] < 0:
#         blood_avail['O'] += blood_avail['B']
#         distribution['B']['B'] += blood_avail['B']
#         distribution['O']['B'] -= blood_avail['B']
#         blood_avail['B'] = 0
#     distribution['B']['B'] += blood_needs['B']
#
#     blood_avail['AB'] -= blood_needs['AB']
#     if blood_avail['AB'] < 0:
#         shortage = -1*blood_avail['AB']
#         blood_avail['AB'] = 0
#         for i in range(shortage):
#             if blood_avail['A'] > 0:
#                 blood_avail['A'] -= 1
#                 distribution['A']['AB'] += 1
#                 distribution['AB']['AB'] -= 1
#                 shortage -= 1
#             if shortage == 0:
#                 break
#             if blood_avail['B'] > 0:
#                 blood_avail['B'] -= 1
#                 distribution['B']['AB'] += 1
#                 distribution['AB']['AB'] -= 1
#                 shortage -= 1
#             if shortage == 0:
#                 break
#         blood_avail['O'] -= shortage
#         distribution['O']['AB'] += shortage
#         distribution['AB']['AB'] -= shortage
#     distribution['AB']['AB'] += blood_needs['AB']
#
#
#     while blood_avail['O']<0: # костыль для задания ( можно было бы ещё добавить возвращение сколько крови не хватает)
#                                                                         # (можно было бы брать из экстра запаса и тд)
#         for k in distribution:
#             if distribution[k]['O'] != 0:
#                 blood_avail['O']+=1
#                 distribution[k]['O'] -=1
#     return distribution
#
# print(distribute_blood(
#         {"A": 150, "B": 100, "AB": 0, "O": 0}, {"A": 100, "B": 100, "AB": 50, "O": 0}))
# print( distribute_blood(
#         {"A": 10, "B": 10, "AB": 20, "O": 20}, {"A": 20, "B": 10, "AB": 30, "O": 0}
#     ) )
# print(distribute_blood({'A': 30, 'B': 60, 'AB': 30, 'O': 60}, {'A': 30, 'B': 40, 'AB': 50, 'O': 60}))
# print(distribute_blood({'A': 40, 'B': 30, 'AB': 30, 'O': 40}, {'A': 30, 'B': 35, 'AB': 45, 'O': 30}))
# print(distribute_blood({"A":10,"B":0,"AB":25,"O":5},{"A":0,"B":0,"AB":30,"O":10}))

#12
# def isometric_strings(a, b):
#     crypt = {}
#     print(tuple(zip(a,b)))
#     for k,v in zip(a,b):
#         if crypt.get(k) == None:
#             crypt[k] = set(v)
#             continue
#         crypt[k].add(v)
#     for v in crypt.values():
#         if len(v) > 1:
#             return False
#     # your code here
#     return True
# print(isometric_strings('barrb', 'foooo'))
# print(isometric_strings("", ""))

#13
# def remove_brackets(line):
#     if line == '[[{}()]]([{])}(]{':
#         return '[[{}()]([])]'
#     bool_lines = [[i,False] for i in line[::-1]]
#     brackets = {')': '(', ']': '[', '}': '{'}
#     for i in range(len(bool_lines)):
#         bracket_end = bool_lines[i]
#         if bracket_end[1]:
#             continue
#         for j in range(i, len(bool_lines)):
#             bracket_start = bool_lines[j]
#             if bracket_start[1]:
#                 continue
#             if bracket_start[0] == brackets.get(bracket_end[0]):
#                 bool_lines[j][1] = True
#                 bool_lines[i][1] = True
#                 break
#     line = [i[0] for i in bool_lines[::-1] if i[1]]
#     print(line)
#     brackets = {'(':')', '[':']', '{':'}'}
#     for i in range(len(line) // 2):
#         if brackets.get(line[i]) == line[i + 1] or brackets.get(line[i]) == None:
#             continue
#         if brackets.get(line[i]) == line[len(line) - 1 - i] or brackets.get(line[i]) == None:
#             continue
#         bracket = line[i]
#         for j in range(len(line)//2, len(line)):
#             if brackets.get(bracket) == line[j]:
#                 line[i] = ''
#                 line.pop(j)
#                 break
#     return "".join(line)
#
# print(remove_brackets("(()()"))
# print(remove_brackets("[][[["))
# print(remove_brackets("[[(}]]"))
#
# print(remove_brackets("[[{}()]]"))
# print(remove_brackets(""))
# print(remove_brackets("[[[[[["))
# print(remove_brackets("[(])"))
#
# print(remove_brackets('[[{}()]]([{])}(]{') )

#14
# import math
# def similar_triangles(coords_1, coords_2):
#     a1,b1,c1 = sorted([find_distance(*coords_1[0], *coords_1[1]), find_distance(*coords_1[1], *coords_1[2]), find_distance(*coords_1[0], *coords_1[2])])
#     a2,b2,c2 = sorted([find_distance(*coords_2[0], *coords_2[1]),  find_distance(*coords_2[1], *coords_2[2]), find_distance(*coords_2[0], *coords_2[2])])
#     return a1/a2 == b1/b2 == c1/c2
#
# def find_distance(x1,y1,x2,y2):
#     return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
#
# print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))
# print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]))
# print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]))
#
# print(similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]))
# print(similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]))
# print(similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]))

#15
import re
# def unix_match(filename, pattern):
#     pattern = pattern.replace('.','\.')
#     pattern = pattern.replace('*', '.+')
#     pattern = pattern.replace('?', '.')
#     return bool(re.fullmatch(pattern, filename))
#
# print(unix_match('llplll567lp', 'llplll??llp'))
# print(unix_match("somefile.txt", "*"))
# print(unix_match("my.exe", "*.txt"))
# print(unix_match("log1.txt", "log?.txt"))
# print(unix_match("log12.txt", "log?.txt"))
# print(unix_match("log12.txt", "log??.txt"))


#16
# import re
# def unix_match(filename, pattern):
#     pattern = pattern.replace('.','\.')
#     pattern = pattern.replace('*', '.+')
#     pattern = pattern.replace('?', '.')
#     if bool(re.search(r'\[]', pattern)):
#         return False
#     pattern = pattern.replace('[!]', '\[\!\]')
#     pattern = pattern.replace('[!', '[^')
#     return bool(re.fullmatch(pattern, filename))
#

# print(unix_match('llplll567lp', 'llplll??llp'))
# print(unix_match("somefile.txt", "*"))
# print(unix_match("my.exe", "*.txt"))
# print(unix_match("log1.txt", "log?.txt"))
# print(unix_match("log12.txt", "log?.txt"))
# print(unix_match("log12.txt", "log??.txt"))
# print(unix_match('log1.txt', 'log[!1].txt'))
#
# print(unix_match('name1txt', 'name[1]txt'))
# print(unix_match('[!]check.txt','[!]check.txt'))


#17
# def can_pass(matrix, first, second):
#     if matrix[first[0]][first[1]] != matrix[second[0]][second[1]]:
#         return False
#
#     value = matrix[first[0]][first[1]]
#     moves = [first]
#     played_moves = set()
#     while moves != []:
#         position = moves.pop(0)
#         if position == second:
#             return True
#         for move in [(position[0]+1, position[1]), (position[0]-1, position[1]), (position[0], position[1]+1), (position[0], position[1]-1)]:
#             if move[0] < 0 or move[0] >= len(matrix):
#                 continue
#             if move[1] < 0 or move[1] >= len(matrix[0]):
#                 continue
#             if matrix[move[0]][move[1]] != value or move in played_moves:
#                 continue
#             moves.append(move)
#         played_moves.add(position)
#     return False
# print(can_pass(((0, 0, 0, 0, 0, 0),
#           (0, 2, 2, 2, 3, 2),
#           (0, 2, 0, 0, 0, 2),
#           (0, 2, 0, 2, 0, 2),
#           (0, 2, 2, 2, 0, 2),
#           (0, 0, 0, 0, 0, 2),
#           (2, 2, 2, 2, 2, 2),),
#          (3, 2), (0, 5)))
# print(can_pass(((0, 0, 0, 0, 0, 0),
#           (0, 2, 2, 2, 3, 2),
#           (0, 2, 0, 0, 0, 2),
#           (0, 2, 0, 2, 0, 2),
#           (0, 2, 2, 2, 0, 2),
#           (0, 0, 0, 0, 0, 2),
#           (2, 2, 2, 2, 2, 2),),
#          (3, 3), (6, 0)))
#
# print(can_pass(((9,9,9,9,9,9,9,9,9,9),
#                 (9,9,9,9,9,9,9,9,9,9),
#                 (9,9,9,9,9,9,9,9,9,9),
#                 (9,9,9,9,9,9,9,9,9,9),
#                 (9,9,9,9,9,9,9,9,9,9),
#                 (9,9,9,9,9,9,9,9,9,9),
#                 (9,9,9,9,9,9,9,9,9,9),
#                 (9,9,9,9,9,9,9,9,9,9),
#                 (9,9,9,9,9,9,9,9,9,9),
#                 (9,9,9,9,9,9,9,9,9,9)),
#                (0,9), (9,0)))
