#1
# class Car:
#     pass
# my_car = Car()

#2
# class Car:
#     wheels = "four"
#     doors = 4
# my_car = Car()

#3
# class Car:
#     def __init__(self, brand='', model=''):
#         self.brand = brand
#         self.model = model
#     wheels = "four"
#     doors = 4
# my_car = Car()
# some_car1 = Car('Ford','Mustang')
# some_car2 = Car(model='Camaro')

#4
# class Car:
#     wheels = "four"
#     doors = 4
#     working_engine = False
#     def __init__(self, brand='', model=''):
#         self.brand = brand
#         self.model = model
#     def start_engine(self):
#         print("Engine has started")
#         self.working_engine = True
#     def stop_engine(self):
#         print("Engine has stopped")
#         self.working_engine = False
# my_car = Car()
# some_car1 = Car('Ford', 'Mustang')
# some_car2 = Car(model='Camaro')
# some_car1.start_engine()
# some_car2.start_engine()

#5
# class Car:
#     wheels = "four"
#     doors = 4
#     working_engine = False
#     def __init__(self, brand='', model=''):
#         self.brand = brand
#         self.model = model
#     def start_engine(self):
#         print("Engine has started")
#         self.working_engine = True
#     def stop_engine(self):
#         print("Engine has stopped")
#         self.working_engine = False
# my_car = Car()
# some_car1 = Car('Ford', 'Mustang')
# some_car2 = Car(model='Camaro')
# some_car1.start_engine()
# some_car2.start_engine()
#
# class ElectricCar(Car):
#     def __init__(self, battery_capacity, brand='', model=''):
#         self.battery_capacity = battery_capacity
#         super().__init__(brand, model)
# my_electric_car = ElectricCar(100, 'Tesla', 'Model 3')

#6,7
# class Car:
#     wheels = "four"
#     doors = 4
#     working_engine = False
#     def __init__(self, brand='', model='',fuel_consumption=7):
#         self.fuel_used = 0
#         self.fuel_consumption = fuel_consumption
#         self.brand = brand
#         self.model = model
#     def start_engine(self):
#         print("Engine has started")
#         self.working_engine = True
#     def stop_engine(self):
#         print("Engine has stopped")
#         self.working_engine = False
#     def drive(self,distance):
#         if not self.working_engine:
#             print("Start the car before driving!")
#             return
#         self.fuel_used += distance/100 * self.fuel_consumption
#         print(f"Currently driven {distance} km, total fuel used - {self.fuel_used} l")
# my_car = Car()
# some_car1 = Car('Ford', 'Mustang')
# some_car2 = Car(model='Camaro')
# some_car1.start_engine()
# some_car2.start_engine()
# class ElectricCar(Car):
#     def __init__(self, battery_capacity, brand='', model=''):
#         self.battery_capacity = battery_capacity
#         super().__init__(brand, model)
#     def start_engine(self):
#         print("Electric motor has started")
#         self.working_engine = True
#     def stop_engine(self):
#         print("Electric motor has stopped")
#         self.working_engine = False
#     def drive(self,distance):
#         if not self.working_engine:
#             print("Start the car before driving!")
#             return
#         print(f"Currently driven {distance} km on electric motor")
# my_electric_car = ElectricCar(100, 'Tesla', 'Model 3')
# my_electric_car.start_engine()
# my_electric_car2 = ElectricCar(60, "Toyota", "Prius")
# my_electric_car2.start_engine()
# my_electric_car2.stop_engine()

#8
# from collections import OrderedDict
# def ryerson_letter_grade(pct):
#     grade = OrderedDict(
#         {90: 'A+', 85: 'A', 80: 'A-', 77: 'B+', 73: 'B', 70: 'B-', 67: 'C+', 63: 'C', 60: 'C-', 57: 'D+', 53: 'D',
#          50: 'D-', 0: 'F'})
#     for key in grade:
#         if pct>=key:
#             return grade[key]
#
# print(ryerson_letter_grade(45) == "F")
# print(ryerson_letter_grade(62) == "C-")

#9
# import string
# def checkio(data):
#     return len(data) >=10 and len(set(data) & set(string.digits))!=0 and len(set(data) & set(string.ascii_lowercase))!=0 and len(set(data) & set(string.ascii_uppercase))!=0

#10
# def sum_consecutives(cons):
#     if len(cons)<2:
#         return cons
#     result = []
#     prev = cons[0]
#     counter = 1
#     for i in cons[1:]:
#         if i != prev:
#             result.append(counter*prev)
#             counter=0
#         counter+=1
#         prev = i
#     result.append(counter*prev)
#     return result
# print(sum_consecutives([1, 1, 1, 1]))
# print(sum_consecutives([1, 1, 2, 2]))
# print(sum_consecutives([3, 3, 3, 4, 4, 5, 6, 6]))


#11
# import math as m
# def simple_areas(*args):
#     if len(args) == 1:
#         return m.pi*(args[0]**2)/4
#     elif len(args)==2:
#         return args[0]*args[1]
#     elif len(args) == 3:
#         p = sum(args)/2
#         return m.sqrt(p*(p-args[0])*(p-args[1])*(p-args[2]))
#
# print(simple_areas(1.5, 2.5, 2))

#12
# def checkio(buildings):
#     buildings.sort(key=lambda x: x[1])
#     heights = {i[4]:set() for i in buildings}
#     visible = len(buildings)
#     for building in buildings:
#         visible_points = set(range(building[0],building[2])) - heights.get(building[4])
#         if len(visible_points)==0:
#             visible-=1
#         for height in [key for key in heights if key<=building[4]]:
#             for point in visible_points:
#                 heights[height].add(point)
#     return visible
#
# print(checkio([
#         [1, 1, 4, 5, 3.5],
#         [2, 6, 4, 8, 5],
#         [5, 1, 9, 3, 6],
#         [5, 5, 6, 6, 8],
#         [7, 4, 10, 6, 4],
#         [5, 7, 10, 8, 3]
#         ]))
# print(checkio([
#         [1, 1, 11, 2, 2],
#         [2, 3, 10, 4, 1],
#         [3, 5, 9, 6, 3],
#         [4, 7, 8, 8, 2]
#         ]))
# print(checkio([
#         [1, 1, 3, 3, 6],
#         [5, 1, 7, 3, 6],
#         [9, 1, 11, 3, 6],
#         [1, 4, 3, 6, 6],
#         [5, 4, 7, 6, 6],
#         [9, 4, 11, 6, 6],
#         [1, 7, 11, 8, 3.25]
#         ]))

#13

# def checkio(land_map):
#     result = []
#     checked = []
#     for row in range(len(land_map)):
#         for col in range(len(land_map[row])):
#             if land_map[row][col] == 0 or (row,col) in checked:
#                 continue
#             area = 0
#             next_to_check = [(row,col)]
#             while next_to_check!=[]:
#                 i, j = next_to_check.pop(0)
#                 area+=1
#                 checked.append((i,j))
#                 all_ways = [(i,j+1), (i,j-1), (i+1,j), (i-1,j), (i+1,j+1), (i-1,j-1), (i+1, j-1),(i-1,j+1)]
#                 # here we add only the ways, which are not checked and not in the queue, equals to 1 and in boundary
#                 next_to_check.extend([way for way in all_ways if 0<=way[0]<len(land_map) and 0<=way[1]<len(land_map[row]) and land_map[way[0]][way[1]]==1 and way not in checked and way not in next_to_check])
#             result.append(area)
#     return sorted(result)
#
# print(checkio([[0, 0, 0, 0, 0],
#                    [0, 0, 1, 1, 0],
#                    [0, 0, 0, 1, 0],
#                    [0, 1, 0, 0, 0],
#                    [0, 0, 0, 0, 0]]))
# print(checkio([
#     [0, 0, 0, 0, 0, 0],
#     [1, 0, 0, 1, 1, 1],
#     [1, 0, 0, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0, 0]]))
# print(checkio([
#     [0, 0, 0, 0, 0],
#     [0, 0, 1, 1, 0],
#     [0, 0, 0, 1, 0],
#     [0, 1, 1, 0, 0]]))


# 14
# def fused_cubes(cubes):
#     result = []
#     for j in range(len(cubes)):
#         cube = all_cords(cubes[j])
#         part_of = None          # that part of the result is this cube part of
#         no_need_vol = []        # everything that was absorbed by another cube
#         for i in range(len(result)):
#             taken = result[i]
#             # intersection of the previous figure's points with the current cube's
#             common_points = {x for xs in taken for x in xs} & {x for xs in cube for x in xs}
#
#             x_cord,y_cord,z_cord = set(),set(),set()
#             for point in common_points: # unique coordinates for x,y,z
#                 x_cord.add(point[0])
#                 y_cord.add(point[1])
#                 z_cord.add(point[2])
#             # we check if the new cube is a part of the checked volume  (if more than 2 coordinates change)
#             if (len(x_cord)>1 and len(y_cord)>1)or(len(x_cord)>1 and len(z_cord)>1)or(len(y_cord)>1 and len(z_cord)>1):
#                 if part_of is None:
#                     result[i] = taken | cube
#                     part_of = i             # sets which volume the cube belongs to
#                 else:
#                     result[part_of] = result[part_of] | taken
#                     no_need_vol.append(i)               # show that this volume was absorbed by another one
#         result = [result[i] for i in range(len(result)) if i not in no_need_vol] # del all indexes, that are not needed
#
#         if part_of is None:     # if the cube doesn't belong to any volume, we set its volume as a new one
#             result.append(cube)
#     return [len(i) for i in result]     # transfer from coordinates of 1x1 cubes to their volume
#
#
# def all_cords(cube):
#     result = set()
#     for z in range(cube[3]):
#         for y in range(cube[3]):
#             for x in range(cube[3]):
#                 x_cord, y_cord, z_cord = (cube[0]+x, cube[1]+y, cube[2]+z)
#                 result.add(((x_cord,y_cord,z_cord),(x_cord+1,y_cord,z_cord),(x_cord,y_cord+1,z_cord),   # tuple of all edges of a box
#                             (x_cord,y_cord,z_cord+1),(x_cord+1,y_cord+1,z_cord),(x_cord+1,y_cord,z_cord+1),
#                             (x_cord,y_cord+1,z_cord+1),(x_cord+1,y_cord+1,z_cord+1),))
#     return result
# print(len(all_cords((0,0,0,3))))
#
#
# print(fused_cubes([(0, 0, 0, 3), (1, 2, 2, 3)]))
# print(fused_cubes([(0, 0, 0, 3), (1, 3, 2, 3)]))
# print(fused_cubes([(0, 0, 0, 3), (1, 3, 3, 3)]))
# print(fused_cubes([[0, 0, 0, 3], [-2, -2, -2, 3]]))
# print(fused_cubes([[-1,0,0,1],[1,0,0,1],[0,1,0,1],[0,-1,0,1],[0,0,1,1],[0,0,-1,1]]))
# print(fused_cubes([[0,0,0,1],[0,1,0,1],[0,2,0,1],[0,3,0,1],[0,5,0,1],[-1,4,0,1],[0,4,0,1],[1,4,0,1],[2,4,0,1],[3,4,0,1],[4,4,0,1],[5,4,0,1],[-1,6,0,1],[0,6,0,1],[1,6,0,1],[2,6,0,1],[3,6,0,1],[4,6,0,1],[5,6,0,1],[4,0,0,1],[4,1,0,1],[4,2,0,1],[4,3,0,1],[4,5,0,1],[2,5,0,1]]))
# print(fused_cubes([[-9,0,0,2],[-9,2,0,2],[-5,0,1,2],[-5,2,1,2],[-1,0,2,2],[-1,2,2,2],[3,0,3,2],[3,2,3,2],[7,0,2,2],[7,2,2,2],[6,3,2,2],[4,3,2,2],[2,3,3,2],[0,3,3,2],[-2,3,2,2],[-4,3,2,2],[-2,0,-7,2],[0,0,0,1],[0,1,0,1],[3,0,-1,1],[3,1,-1,1]]))
# print(fused_cubes([[-4,0,-4,2],[-2,0,-4,2],[0,0,-4,2],[2,0,-4,2],[2,0,-2,2],[2,0,0,2],[2,0,2,2],[-3,2,-3,2],[-1,2,-3,2],[1,2,-3,2],[1,2,-1,2],[1,2,1,2],[-2,4,-2,2],[0,4,-2,2],[0,4,0,2],[-1,0,-5,1],[0,0,-5,1],[-1,1,-4,2],[-1,3,-3,2],[4,0,-1,1],[4,0,0,1],[2,1,-1,2],[1,3,-1,2],[-1,6,-1,2]]))

#15
# def count_gold(pyramid):
#     work = list(list(row) for row in pyramid)
#     for i in range(len(work) - 1, 0, -1):
#         for j in range(len(work[i])-1):
#             left = work[i][j]
#             right = work[i][j+1]
#             work[i-1][j] += max(left,right)
#     return work[0][0]
# print(count_gold(
#         [
#             [1],
#             [2, 3],
#             [3, 3, 1],
#             [3, 1, 5, 4],
#             [3, 1, 3, 1, 3],
#             [2, 2, 2, 2, 2, 2],
#             [5, 6, 4, 5, 6, 4, 3],
#         ]
#     ))
# print(count_gold([[9], [2, 2], [3, 3, 3], [4, 4, 4, 4]]) == 18)
# print(count_gold(
#         [
#             [1],
#             [2, 1],
#             [1, 2, 1],
#             [1, 2, 1, 1],
#             [1, 2, 1, 1, 1],
#             [1, 2, 1, 1, 1, 1],
#             [1, 2, 1, 1, 1, 1, 9],
#         ]
#     )==15)
# print(count_gold(
#         [[2], [7, 9], [0, 8, 6], [4, 7, 6, 8], [0, 5, 5, 4, 1], [9, 1, 0, 1, 6, 9]]
#     ))

#16         ! Not My Solution !
# def unfair_districts(number, data):
#     height, width = len(data), len(data[1])
#     valid = {(x, y) for y in range(width) for x in range(height)}
#     out = [['']*width for _ in range(height)]
#     stack = [((0, 0), [((0,0),)])]
#     while stack:
#         (x, y), area = stack.pop()
#         # print(x,y)
#         print(stack)
#         if len(sum(area, ())) == height*width:
#             wins, loses = 0, 0
#             for i in area:
#                 a = sum([data[x][y][0] for x, y in i])
#                 b = sum([data[x][y][1] for x, y in i])
#                 wins, loses = wins+(a > b), loses+(a < b)
#             if wins <= loses: continue
#             for k, i in enumerate(area):
#                 for a, b in i: out[a][b] = str(k)
#             return [''.join(j) for j in out]
#         last_group = area.pop()
#         print(last_group)
#         group_sum = sum(sum([data[i][j] for i, j in last_group], []))
#         if group_sum > number:
#             continue
#         if group_sum == number:
#             area, last_group = area+[last_group], ()
#         neighbors = {(x+1, y), (x-1, y), (x, y+1), (x, y-1)} & valid
#         for i in (neighbors - set(sum(area, ())+last_group)):
#             stack += [(i, area+[last_group+(i,)])]
#             if len(last_group) in [1, 2]:
#                 stack += [(last_group[-1], area+[last_group+(i,)])]
#     return []
#
# print(unfair_districts(5, [[[2, 1], [1, 1], [1, 2]],
#                      [[2, 1], [1, 1], [0, 2]]]))

#17
# def digit_stack(commands):
#     sum_elem = 0
#     stack = []
#     for command in commands:
#         try:
#             if command == 'POP':
#                 sum_elem += stack.pop()
#             elif command == 'PEEK':
#                 sum_elem += stack[-1]
#             else:
#                 stack.append(int(command[-1]))
#         except IndexError:
#             pass
#     return sum_elem
# print(digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]))
# print(digit_stack(["POP", "POP"]))
# print(digit_stack(["PUSH 9", "PUSH 9", "POP"]))
# print(digit_stack([]))

#18
# import re
# def double_substring(line):
#     return max([len(i) for i in re.findall(r'(?=(.*).*\1)', line)])
# print(double_substring("aghtfghkofgh"))

#19
from collections import namedtuple
def checkio(field_map):
    field_map = [list(f) for f in field_map]
    W = len(field_map[0])
    H = len(field_map)
    def next_steps(row, col):
        result = []

        if row+1 < H and field_map[row+1][col] != "W":
            result.append("D")
        if row-1 >= 0 and field_map[row-1][col] != "W":
            result.append("U")
        if col+1 < W and field_map[row][col+1] != "W":
            result.append("R")
        if col-1 >= 0 and field_map[row][col-1] != "W":
            result.append("L")
        if field_map[row][col] == "B":
            result.append("B")
        return result

    def make_move(position, move):
        i, j, path, price, load = position
        if move == 'R':
            return rated_path(i, j+1, path+"R", price+2 if load else price+1, load)
        if move == 'L':
            return rated_path(i, j-1, path+"L", price+2 if load else price+1, load)
        if move == 'U':
            return rated_path(i-1, j, path+"U", price+2 if load else price+1, load)
        if move == 'D':
            return rated_path(i+1, j, path+"D", price+2 if load else price+1, load)
        if move == 'B':
            return rated_path(i, j, path+"B", price+1, False if load else True)

    rated_path = namedtuple("rated_path", ("row", "col", "path", "price","loaded"))
    x,y = [(i, field_map[i].index("S")) for i in range(H) if "S" in field_map[i]][0]    # cords of the starting point
    start = rated_path(x,y,path="",price=0, loaded=True)
    paths_to_check = [start]
    checked_path = set()
    while True:
        current = paths_to_check.pop()
        if (current.row, current.col, current.loaded) in checked_path:    # probably not needed
            continue
        # print(current.row, current.col)
        if field_map[current.row][current.col] == "E" and current.loaded:
            return current.path
        for step in next_steps(current.row,current.col):
            next_move = make_move(current, step)
            if (next_move.row, next_move.col, next_move.loaded) not in checked_path:
                paths_to_check.append(next_move)
        checked_path.add((current.row, current.col, current.loaded))  # might be in the wrong place
        paths_to_check.sort(key=lambda x: x.price, reverse=True)

print(checkio(["S...","....","B.WB","..WE"]))
print(checkio(["S...","....","B..B","..WE"]))