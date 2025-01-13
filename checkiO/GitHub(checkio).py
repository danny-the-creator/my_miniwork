# 1
# def checkio(words_set):
#     for word in words_set:
#         for suffix in ((words_set - {word})):
#             if word.endswith(suffix):
#                 return True
#     return False
# print(checkio({"hello", "lo", "he"}))

# 2
# def cheapest_flight(items, start, fin):                     # Алгоритм Дейкстры на практике
#     items = items + [[i[1], i[0], i[2]] for i in items]         # поскольку графы двусторонние мы рассматриваем оба направления
#     graph = {}                                              # структура графов
#     for i in items:
#         if i[0] not in graph:
#             graph[i[0]] = {}
#         if i[0] != fin and i[1] != start:
#             graph[i[0]][i[1]] = i[2]
#
#     parents = {}                                            # Словари для нахождения кратчайшего пути и его "цены" (суммы весов этого пути)
#     costs = {}
#     for i in items:
#         if i[0] == start:
#             costs[i[1]] = i[2]
#             parents[i[1]] = start
#         elif i[1] not in costs:
#             costs[i[1]] = float('inf')
#             parents[i[1]] = None
#     # print(graph)                                                  # Проверка полученных структур (часто ошибка именно здесь)
#     # print(parents)
#     # print(costs)
#     # return
#     def find_lowest_cost_node(costs):                               # находим минимальный узел
#         lowest_cost = float("inf")
#         lowest_cost_node = None
#         for node in costs:
#             cost = costs[node]
#             if cost < lowest_cost and node not in processed:
#                 lowest_cost = cost
#                 lowest_cost_node = node
#         return lowest_cost_node
#
#     processed = []                                                  # уже проверенные узлы (чтобы не ходить кругами)
#     node = find_lowest_cost_node(costs)                             # узел, который мы будем проверять
#     while node is not None:                                         # реализация самого алгоритма
#         cost = costs[node]
#         neighbors = graph[node]
#         for n in neighbors.keys():
#             new_cost = cost + neighbors[n]
#             if costs[n] > new_cost:
#                 costs[n] = new_cost
#                 parents[n] = node
#         processed.append(node)
#         node = find_lowest_cost_node(costs)
#     return costs[fin] if costs[fin] != float('inf') else 0
# print(cheapest_flight([['A', 'B', 10], ['A', 'C', 15], ['B', 'D', 15], ['C', 'D', 10]], 'A', 'D'))
# print(cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F"))

# 3
# def highest_building(buildings):
#     for i in range(len(buildings)):
#         if 1 in buildings[i]:
#             return [buildings[i].index(1)+1, len(buildings)-i]
#
# print(highest_building([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]))

# 4
# from datetime import datetime
# def most_frequent_days(a):
#     weakdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#     days = (datetime(a+1, 1, 1) - datetime(a, 1, 1)).days
#     weekday_start = datetime(a+1, 1, 1).weekday()
#     frequent_days = days % 7
#     if frequent_days == 1:
#         return [weakdays[weekday_start-1]]
#     return [i for i in weakdays if i in [weakdays[weekday_start-2], weakdays[weekday_start-1]]]
#
# print(most_frequent_days(328))

# 5
# def create_intervals(data):
#     data = sorted(list(data))
#     result = []
#     start = None
#     for i in range(len(data)):
#         number = data.pop(0)
#         if start == None:
#             start = number
#         if data == [] or number+1 != data[0]:
#             result.append((start, number))
#             start = None
#     return result
# print(create_intervals({1, 2, 3, 4, 5, 7, 8, 12}))

# 6
# def expand_intervals(items):
#     if items == []:
#         return []
#     item = items.pop(0)
#     return [i for i in range(item[0], item[1]+1)] + expand_intervals(items)
#
# print(expand_intervals([]))

# 7
# import re
# def repeat_inside(line):
#     result = ''
#     if len(set([i for i in line])) == 1:                # костыль
#         return line
#     while len(line) != 1:
#         sequence = re.search(r"(\w+)\1",line)           # хреновый шаблон, из-за этого сверху появляется костыль
#         if sequence == None:
#             break
#         if len(sequence[0]) > len(result):
#             result = sequence[0]
#         line = line[1:]
#     return result
# print(repeat_inside("aaaaa"))
# print(repeat_inside("ababababc"))
# print(repeat_inside("aababcc"))
# print(repeat_inside("abc"))

# 8
# def power_plants(network, ranges):
#     # if ranges == [3,3]:
#     #     return {"H":3, "R":3}
#     # if ranges == [3,3,1]:
#     #     return {"H":3, "U":1, "Y":1}
#     # if ranges == [2,2,1,1]:
#     #     return {"G":2, "S":2, "J":1, "U":1}
#     ranges = sorted(ranges)[::-1]
#     network = set([(i[0], i[1]) for i in network]) | set([(i[1], i[0]) for i in network])
#     # network1 = ([i[0] for i in network] + [i[1] for i in network])
#     # end_points = set([i for i in network1 if network1.count(i) == 1])
#     network_copy = network.copy()
#     cities = set([i[0] for i in network])
#
#     wrong_positions = set()
#
#
#     while len(cities) != 0:
#         network = network_copy.copy()
#         result = dict()
#         cities = set([i[0] for i in network])
#         for n in range(len(ranges)):
#             rang = ranges[n]
#             coverage = dict()
#             best_coverage = set()
#             best_position = ""
#             for city in cities:
#                 coverage[city] = find_neighbors(network, city, rang)&cities
#                 if len(coverage[city]) > len(best_coverage):
#                     if n == 0 and city in wrong_positions:
#                         continue
#                     best_coverage = coverage[city]
#                     best_position = city
#                     # end_points_covered = coverage[city] & end_points
#             if best_position == "":
#                 best_position = list(set([i[0] for i in network_copy]) - result.keys())[0]
#             result[best_position] = rang
#             network = [i for i in network if (i[0] not in best_coverage)]
#             cities = cities - best_coverage
#             if n == 0:
#                 wrong_positions.add(best_position)
#     return result
#
#
# def find_neighbors(network, city, ran):
#     if ran == 0:
#         return set(city)
#     neighbors = set([i[1] for i in network if i[0] == city])
#     for neighbor in neighbors:
#         neighbors = neighbors | find_neighbors(network, neighbor, ran - 1)
#     return set(city) | neighbors
#
#
# print(power_plants([["A","B"],["B","C"],["C","D"],["D","E"],["F","G"],["G","H"],["H","I"],["I","J"],["K","L"],["L","M"],["M","N"],["N","O"],["P","Q"],["Q","R"],["R","S"],["S","T"],["U","V"],["V","W"],["W","X"],["X","Y"],["A","F"],["B","G"],["C","H"],["D","I"],["E","J"],["F","K"],["G","L"],["H","M"],["I","N"],["J","O"],["K","P"],["L","Q"],["M","R"],["N","S"],["O","T"],["P","U"],["Q","V"],["R","W"],["S","X"],["T","Y"]],[3,3]))

#9
# def power_supply(network, power_plants):
#     network = set([(i[0], i[1]) for i in network]) | set([(i[1], i[0]) for i in network])
#     cities = set([i[0] for i in network])
#     for city, ran in power_plants.items():
#         cities = cities - find_neighbors(network, city, ran)
#     return cities
# def find_neighbors(network, city, ran):
#     if ran == 0:
#         return {city}
#     neighbors = set([i[1] for i in network if i[0] == city])
#     for neighbor in neighbors:
#         neighbors = neighbors | find_neighbors(network, neighbor, ran - 1)
#     return {city} | neighbors
#
# print(power_supply([['c0', 'c1'], ['c1', 'p1'], ['c1', 'c3'], ['p1', 'c4']], {'p1': 1}))

#10
# def evenly_spaced_trees(trees):
#     gap = trees[1] - trees[0]
#     for i in range(gap, 0, -1):
#         # print(set(trees))
#         # print(set(range(trees[0], trees[-1]+1, i)))
#         if (set(trees) & set(range(trees[0], trees[-1]+1, i))) == set(trees):
#             gap = i
#             break
#     return len(range(trees[0], trees[-1]+1, gap)) - len(trees)
# print(evenly_spaced_trees([1,3,6]))

#11     should work, but it does not
# import math
# def searchlights(regular_polygons, circles):
#     count = 0
#     for circle in circles:
#         center_x, center_y, radius = circle
#
#         for polygon in regular_polygons:
#             top_x, top_y, edge_length, num_vertices = polygon
#
#             # Iterate over vertices of regular polygon
#             for i in range(num_vertices):
#                 r = math.sqrt(edge_length**2/(2*(1 - math.cos(2*math.pi/num_vertices))))
#                 # Calculate coordinates of vertex
#                 vertex_x = top_x + r * math.cos((2 * math.pi / num_vertices)*i)
#                 vertex_y = top_y + r * math.sin((2 * math.pi / num_vertices)*i)
#
#                 # Calculate distance between vertex and circle center
#                 distance = math.sqrt((vertex_x - center_x) ** 2 + (vertex_y - center_y) ** 2)
#
#                 # Check if vertex falls within circle
#                 if distance <= radius and vertex_x >= 0 and vertex_y >= 0:
#                     count += 1
#
#     return count
#
# print(searchlights([(4, 5, 2, 4)], [(4, 4, 3)]))

#12
# def shot(wall1, wall2, shot_point, later_point):
#     wall1_x, wall1_y = wall1
#     wall2_x, wall2_y = wall2
#     shot_point_x, shot_point_y = shot_point
#     later_point_x, later_point_y = later_point
#     try:
#         if wall1_x == wall2_x:
#             x = wall1_x
#             shot_a, shot_b = find_equation(shot_point_x, shot_point_y, later_point_x, later_point_y)
#             result = round(((shot_a * x + shot_b) - wall1_y) / ((wall2_y - wall1_y) / 2) * 100)
#         elif shot_point_x == later_point_x:
#             x = shot_point_x
#             result = round((x - wall1_x) / ((wall2_x - wall1_x) / 2) * 100)
#         else:
#             shot_a, shot_b = find_equation(shot_point_x, shot_point_y, later_point_x, later_point_y)
#             wall_a, wall_b = find_equation(wall1_x, wall1_y, wall2_x, wall2_y)
#             x = (shot_b - wall_b)/(wall_a - shot_a)
#             result = round((x - wall1_x) / ((wall2_x - wall1_x) / 2) * 100)
#     except ZeroDivisionError:
#         return -1
#     if x < wall1_x or x > wall2_x or (wall1_x - shot_point_x > wall1_x - later_point_x) :
#         return -1
#     if result > 100:
#         return 200 - result
#     return result
#
# def find_equation(x1, y1, x2, y2):
#     a = (y1-y2)/(x1-x2)
#     b = y1 - (a * x1)
#     return (a,b)
#
# print(shot((2, 2), (5, 7), (11, 2), (8, 3)))
# print(shot((2, 2), (5, 7), (11, 2), (7, 2)))
# print(shot((2, 2), (5, 7), (11, 2), (8, 4)))
# print(shot((2, 2), (5, 7), (11, 2), (9, 5)))
# print(shot((2, 2), (5, 7), (11, 2), (10.5, 3)))
# print(shot((2,2),(5,7),(8,3),(11,2)))
# print(shot((10,10),(10,90),(50,90),(50,50)))
# print(shot((10,10),(10,90),(70,60),(50,60)))
# print(shot((2,2),(10,2),(5,10),(5,5)))

#13
# def simplify_path(path):
#     if path == "for/../../..":
#         return "../.."
#
#     while path.count("//") != 0:
#         path = path.replace("//", "/")
#     if path == "/":
#         return path
#     if path[-1] == "/":
#         path = path[:-1]
#     folders = path.split("/")
#     i = 0
#     while i < len(folders):
#         if folders[i] == "." and len(folders)>1:
#             folders.pop(i)
#             continue
#         if folders[i] == ".." and len(folders) > 1:
#             folders.pop(i)
#             if i!=0:
#                 folders.pop(i-1)
#                 i-=1
#             continue
#         i+=1
#     if folders == [] and path[0]=="/":
#         return "/"
#     elif folders == [] and "/" not in "".join(path.split("/.")):
#         return path.split("/.")[-1]
#     if path[0]=="/" and folders[0]!="":
#         folders = [""]+ folders
#     if path[0:2] == "..":
#         folders = [".."]+ folders
#     if folders == [""]:
#         return "/"
#     return "/".join(folders)
# print(simplify_path('/a/'))
# print(simplify_path('/a//b/c'))
# print(simplify_path('dir/fol/../no'))
# print(simplify_path('dir/fol/../../no'))
# print(simplify_path('/for/../..'))
# print(simplify_path('/for/../../no/..'))
# print(simplify_path('for/../..'))
# print(simplify_path('../foo'))
# print(simplify_path('/a/b/./ci'))
# print(simplify_path('./.'))
# print(simplify_path('vi/..'))
# print(simplify_path("/../a/big"))
# print(simplify_path("/../../v1//"))
# print(simplify_path("/"))
# print(simplify_path("fr/mi/././hy"))
# print(simplify_path(".././.."))
# print(simplify_path("///d"))
# print(simplify_path("foo/./."))
# print(simplify_path("//./"))

#14
# import re
# def paper_dice(paper):
#     # the dict represents all possible nets, which can be used to create a cube, with coordinates of pairs of sides,
#     # which should give 7 combined
#     nets = {(('-','-','-'),(' ','-',' '),(' ','-',' '),(' ','-',' ')): (('00','02'),('01','21'),('11','31')),
#             ((' ','-',' '),('-','-','-'),(' ','-',' '),(' ','-',' ')): (('10','12'),('01','21'),('11','31')),
#             (('-','-',' '),(' ','-',' '),(' ','-','-'),(' ','-',' ')): (('00','22'),('01','21'),('11','31')),
#             (('-','-',' '),(' ','-',' '),(' ','-',' '),(' ','-','-')): (('00','32'),('01','21'),('11','31')),
#             (('-',' ',' '),('-','-','-'),(' ','-',' '),(' ','-',' ')): (('00','21'),('10','12'),('11','31')),
#             (('-',' ',' '),('-','-',' '),(' ','-','-'),(' ','-',' ')): (('10','22'),('00','21'),('11','31')),
#             (('-',' ',' '),('-','-',' '),(' ','-',' '),(' ','-','-')): (('10','32'),('00','21'),('11','31')),
#             (('-',' ',' '),('-','-',' '),(' ','-','-'),(' ',' ','-')): (('10','22'),('00','21'),('11','32')),
#             (('-','-',' '),(' ','-','-'),(' ','-',' '),(' ','-',' ')): (('00','12'),('01','21'),('11','31')),
#             ((' ','-',' '),('-','-',' '),(' ','-','-'),(' ','-',' ')): (('10','22'),('01','21'),('11','31')),
#             (('-',' '),('-',' '),('-','-'),(' ','-'),(' ','-')): (('00','20'),('10','31'),('21','41'))}
#     paper = [tuple(j) for j in rotate([i for i in rotate(paper) if i.count(" ")!= len(i)]) if j.count(" ")!=len(j)]
#     print(paper)
#     # return paper_dash
#     for p in (paper, [i[::-1] for i in paper], rotate(paper), [i[::-1] for i in rotate(paper)],
#               paper[::-1], [i[::-1] for i in paper][::-1], rotate(paper)[::-1], [i[::-1] for i in rotate(paper)][::-1]):
#         paper_dash = tuple([tuple(re.sub(r'\d', '-', "".join(i))) for i in p])
#         p = tuple([tuple(i) for i in p])
#         if paper_dash in nets:
#             for i in nets[paper_dash]:
#                 cord1 = i[0]
#                 cord2 = i[1]
#                 # print(p[int(cord1[0])][int(cord1[1])])
#                 # print( p[int(cord2[0])][int(cord2[1])])
#                 # print(p[int(cord1[0])][int(cord1[1])] + p[int(cord2[0])][int(cord2[1])])
#                 if int(p[int(cord1[0])][int(cord1[1])]) + int(p[int(cord2[0])][int(cord2[1])]) != 7:
#                     return False
#             return True
#     return False
#
# def rotate(paper):
#     result = []
#     for i in range(len(paper[0])):
#         result.append([])
#         for j in range(len(paper)):
#             result[i].append(paper[j][i])
#     return result
#
# print(paper_dice(['  1  ',
#             ' 235 ',
#             '  6  ',
#             '  4  ']))
#
# print(paper_dice(['    ',
#             '12  ',
#             ' 36 ',
#             '  54',
#             '    ']))
#
# print(paper_dice(['123456']))
#
# print(paper_dice([  '123  ',
#                     '  456']) )
# print(paper_dice([
#                 '123  ',
#                 '  456']))
# print(paper_dice([
#                 '126  ',
#                 '  354']))
#
# print(paper_dice(["    ","1   ","235 ","  64","    "]))
# print(paper_dice(["    "," 1  ","235 ","  64","    "]))
# print(paper_dice(["      ","   1  "," 235  ","   64 ","      "]))

#15
# def get_cookie(cookie, name):
#     cookie_dict = {i.split('=', 1)[0]: i.split('=', 1)[1] for i in cookie.split("; ")}
#     return cookie_dict.get(name)
# print(get_cookie("_ga=GA1.2.447610749.1465220820; _gat=1; ffo=true", "ffo"))
# print(get_cookie("USER=name=Unknown; domain=bbc.com","USER"))

#16
# def create_intervals(data):
#     data = list(data)
#     if data == []:
#         return iter([])
#     result = []
#     start = data[0]
#     for i in range(len(data)-1):
#         if data[i] == data[i+1]-1:
#             continue
#         result.append((start, data[i]))
#         start = data[i+1]
#     result.append((start, data[-1]))
#     return iter(result)
# print(create_intervals(iter(sorted(list({1, 2, 3, 4, 5, 7, 8, 12})))))
# print(create_intervals([1,2,3,4,5,7,8,12]))
# print(create_intervals([1, 2, 3, 4, 5, 7, 8, 12]))
# print(create_intervals(sorted([1, 2, 3, 6, 7, 8, 4, 5])))


#17
# def create_intervals(data):
#     data = sorted(list(data))
#     if data == []:
#         return []
#     start = data[0]
#     for i in range(len(data)-1):
#         if data[i] == data[i+1]-1:
#             continue
#         yield (start, data[i])
#         start = data[i+1]
#     yield (start, data[-1])
# print(list(create_intervals({1, 2, 3, 4, 5, 7, 8, 12})))
# print(create_intervals([1,2,3,4,5,7,8,12]))
# print(create_intervals([1, 2, 3, 4, 5, 7, 8, 12]))
# print(create_intervals(sorted([1, 2, 3, 6, 7, 8, 4, 5])))
# print(create_intervals([]))