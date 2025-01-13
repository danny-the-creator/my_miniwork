# 1     doesn't work, but complete
# def visibilities(grid):
#     solution = find_blockers(grid)
#     return [(i, j) for i in range(len(solution)) for j in range(len(solution[0])) if solution[i][j] == "X"]
# # GLOBAL = 0
#
# def find_blockers(grid):
#     # global GLOBAL
#     finish = is_finished(grid)
#     if is_finished(grid):
#         return grid
#     elif finish is None:
#         return
#     valid_moves = get_valid_moves(grid)
#     # GLOBAL+=1
#     # if GLOBAL > 25000 and len(valid_moves)>20:
#     #     print(len(valid_moves))
#     for move in valid_moves:
#         grid_copy = [i.copy() for i in grid]
#         grid_copy[move[0]][move[1]] = "X"
#         sub_moves = find_blockers(grid_copy)
#         if sub_moves is not None:
#             return sub_moves
#
# def is_valid_move(move, grid):
#     row, col = move
#     if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])):
#         return False
#     if grid[row][col] != 0:
#         return False
#     if (col < len(grid[0]) - 1 and grid[row][col + 1] == 'X') or (col > 0 and grid[row][col - 1] == 'X'):
#         return False
#     if (row < len(grid) - 1 and grid[row + 1][col] == 'X') or (row > 0 and grid[row - 1][col] == 'X'):
#         return False
#
#     colored_edges = 0
#     edge_rows = [0, len(grid) - 1]
#     edge_cols = [0, len(grid[0]) - 1]
#     diagonal = []  # all colored boxes diagonally
#     next_to_check = [(row, col)]
#     while next_to_check != []:
#         row_c, col_c = next_to_check.pop(0)
#         if row_c in edge_rows or col_c in edge_cols:
#             colored_edges += 1
#             if colored_edges > 1:
#                 return False
#         diagonal.append((row_c, col_c))
#         diag_path = [(row_c + 1, col_c + 1), (row_c - 1, col_c - 1), (row_c + 1, col_c - 1), (row_c - 1, col_c + 1)]
#         next_to_check.extend([i for i in diag_path if (0 <= i[0] < len(grid)) and (0 <= i[1] < len(grid[0])) and (
#                 grid[i[0]][i[1]] == 'X') and i not in diagonal])
#     return True
#
#
# def get_valid_moves(grid):
#     valid_moves = []
#     for row in range(len(grid)):
#         for col in range(len(grid[1])):
#             if is_valid_move((row, col), grid):
#                 valid_moves.append((row, col))
#     return valid_moves
#
#
# def is_finished(grid):
#     coverage = [((row, col), grid[row][col]) for row in range(len(grid)) for col in range(len(grid[0])) if
#                 grid[row][col] != 0 and grid[row][col] != 'X']
#     for point in coverage:
#         row, col = point[0]
#         value = point[1]
#         counter = 1  # the box itself
#         for vector in ((0, 1), (0, -1), (1, 0), (-1, 0)):
#             i, j = row, col
#             while counter <= value and (0<=i+vector[0]<=len(grid) - 1) and (0<=j+vector[1]<= len(grid[0]) - 1):
#                 i += vector[0]
#                 j += vector[1]
#                 if grid[i][j] == 'X':
#                     break
#                 counter += 1
#         if counter < value:
#             return None
#         if counter > value:
#             return False
#     return True
#
# print(find_blockers([[0,0,0,0,0,0,4,7],
#                     [0,0,0,0,4,0,3,0],
#                     [0,0,8,0,0,7,0,0],
#                     [0,4,0,6,0,0,0,0],
#                     [6,5,0,0,0,0,0,0]]))

# print(visibilities(([       [0, 0,  4,  0,  6],
#                             [0 , 7, 0, 0,  0],
#                             [0, 0, 0, 0, 0],
#                             [0  , 0, 0,  6, 0],
#                             [7  , 0, 8,  0,  0],
#                              [0  , 0, 0,  0,  0]])))

# 2 Not my code, but simply uses recursion,however the trivial case is pretty hard to understand(sometimes doesn't work)
# from itertools import product
# from copy import deepcopy
#
# def is_correct(x, y, grid, final=False):
#     ''' Verify if there is any cycle starting from position x, y also
#         for the final solution check if all fields are visited '''
#
#     height, width = len(grid), len(grid[0])
#     stack, visited = [((-1, -1), (x, y))], set()
#     while stack:
#         prev, (x, y) = stack.pop()
#         if (x, y) in visited:
#             return False
#         if len(grid[x][y]) > 1:
#             continue
#         visited |= {(x, y)}
#         for direct in list(grid[x][y])[0]:
#             stack += [((x, y), (x - 1, y))] * (direct == 'N' and (x - 1, y) != prev)
#             stack += [((x, y), (x + 1, y))] * (direct == 'S' and (x + 1, y) != prev)
#             stack += [((x, y), (x, y - 1))] * (direct == 'W' and (x, y - 1) != prev)
#             stack += [((x, y), (x, y + 1))] * (direct == 'E' and (x, y + 1) != prev)
#
#     return len(visited) == height * width if final else True
#
#
# def solve(grid, data):
#     ''' Firstly try to find out fields that can be easily solved '''
#
#     height, width = len(grid), len(grid[0])
#     last_solved, solved = -1, 0
#     while last_solved < solved:
#         last_solved, solved = solved, 0
#         for x, y in product(range(height), range(width)):
#             if not data[x][y]:
#                 return
#             if len(data[x][y]) > 1:
#                 continue
#             solved += 1
#             neighbors = [(x - 1, y, 'NS'), (x + 1, y, 'SN')]
#             neighbors += [(x, y + 1, 'EW'), (x, y - 1, 'WE')]
#             for nx, ny, (a, b) in neighbors:
#                 if a in data[x][y][0]:
#                     data[nx][ny] = [z for z in data[nx][ny] if b in z]
#                 elif 0 <= nx < height and 0 <= ny < width:
#                     data[nx][ny] = [z for z in data[nx][ny] if b not in z]
#
#     if solved == height * width:
#         if not is_correct(0, 0, data, True):
#             return
#         return [[x[0] for x in y] for y in data]
#
#     ''' Not all fields are solved we need to branch off '''
#     for x, y in product(range(height), range(width)):
#         if len(data[x][y]) > 1:
#             break
#
#     for option in data[x][y]:
#         branch = deepcopy(data)
#         branch[x][y] = [option]
#         if not is_correct(x, y, branch):
#             continue
#         solution = solve(grid, branch)
#         if solution:
#             return solution
#
#
# def checkio(grid):
#     rotation = {'E': 'ESWN', 'N': 'NESW', 'S': 'SWNE', 'W': 'WNES'}
#     height, width = len(grid), len(grid[0])
#     data = [[''] * width for _ in range(height)]
#
#     ''' init data with correct values '''
#     for x, y in product(range(height), range(width)):
#         variations = zip(*[list(rotation[p]) for p in sorted(grid[x][y])])
#         data[x][y] = {''.join(sorted(x)) for x in variations}
#         neighbors = [(x + 1, y, 'S'), (x - 1, y, 'N'), (x, y + 1, 'E'), (x, y - 1, 'W')]
#         for nx, ny, direct in neighbors:
#             if not (0 <= nx < height and 0 <= ny < width):
#                 data[x][y] = [r for r in data[x][y] if direct not in r]
#
#     return solve(grid, data)


# 3
# def unruly(grid):     МОЁ!!! работает)
#     grid = [list(s) for s in grid]
#     legal_positions = [(i,j) for i in range(len(grid)) for j in range(len(grid[i])) ]
#     colored_positions = {(i,j, grid[i][j]) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] != '.'}
#     rows = {r: {"B":set(), "W":set()} for r in range(len(grid))}
#     cols = {c: {"B":set(), "W":set()} for c in range(len(grid[0]))}
#     while len(colored_positions) < len(grid)*len(grid[0]):
#
#         for r,c,color in colored_positions:
#             cols[c][color].add(r)
#             rows[r][color].add(c)
#
#         for row, v in rows.items():
#             if len(v["B"]) == len(grid[0])/2:
#                 for col in range(len(grid[0])):
#                     value = (row, col, "W")
#                     if value not in colored_positions and (row, col, "B") not in colored_positions:
#                         colored_positions.add(value)
#                         cols[col]["W"].add(row)
#                         grid[value[0]][value[1]] = value[2]
#             if len(v["W"]) == len(grid[0])/2:
#                 for col in range(len(grid[0])):
#                     value = (row, col, "B")
#                     if value not in colored_positions and (row, col, "W") not in colored_positions:
#                         colored_positions.add(value)
#                         cols[col]["B"].add(row)
#                         grid[value[0]][value[1]] = value[2]
#
#             if len(v["B"])+1 == len(grid[0])/2:
#                 for col in range(len(grid[0])-2):
#                     if {(row, col, "B"), (row, col + 1, "B"), (row, col + 2, "B")} & colored_positions == set():
#                         for c in range(len(grid[0])):
#                             if c not in (col, col+1, col+2) and (row, c, "B") not in colored_positions:
#                                 colored_positions.add((row, c, "W"))
#                                 cols[c]["W"].add(row)
#                                 grid[row][c] = "W"
#             if len(v["W"])+1 == len(grid[0]) / 2:
#                 for col in range(len(grid[0]) - 2):
#                     if {(row, col, "W"), (row, col + 1, "W"), (row, col + 2, "W")} & colored_positions == set():
#                         for c in range(len(grid[0])):
#                             if c not in (col, col + 1, col + 2) and (row, c, "W") not in colored_positions:
#                                 colored_positions.add((row, c, "B"))
#                                 cols[c]["B"].add(row)
#                                 grid[row][c] = "B"
#
#         for col, v in cols.items():
#             if len(v["B"]) == len(grid)/2:
#                 for row in range(len(grid)):
#                     value = (row, col, "W")
#                     if value not in colored_positions and (row, col, "B") not in colored_positions:
#                         colored_positions.add(value)
#                         rows[row]["W"].add(col)
#                         grid[value[0]][value[1]] = value[2]
#             if len(v["W"]) == len(grid)/2:
#                 for row in range(len(grid)):
#                     value = (row, col, "B")
#                     if value not in colored_positions and (row, col, "W") not in colored_positions:
#                         colored_positions.add(value)
#                         rows[row]["B"].add(col)
#                         grid[value[0]][value[1]] = value[2]
#             if len(v["B"])+1 == len(grid)/2:
#                 for row in range(len(grid) - 2):
#                     if {(row, col, "B"), (row + 1, col, "B"), (row + 2, col, "B")} & colored_positions == set():
#                         for r in range(len(grid)):
#                             if r not in (row, row + 1, row + 2) and (r, col, "B") not in colored_positions:
#                                 colored_positions.add((r, col, "W"))
#                                 rows[r]["W"].add(col)
#                                 grid[r][col] = "W"
#             if len(v["W"])+1 == len(grid) / 2:
#                 for row in range(len(grid) - 2):
#                     if {(row, col, "W"), (row + 1, col, "W"), (row + 2, col, "W")} & colored_positions == set():
#                         for r in range(len(grid)):
#                             if r not in (row, row + 1, row + 2) and (r, col, "W") not in colored_positions:
#                                 colored_positions.add((r, col, "B"))
#                                 rows[r]["B"].add(col)
#                                 grid[r][col] = "B"
#         if len(colored_positions) == len(grid)*len(grid[0]):
#             break
#
#
#
#
#
#         for p in colored_positions.copy():
#             if (p[0], p[1]+1, p[2]) in colored_positions and (p[0], p[1]-1) in legal_positions:
#                 value = (p[0], p[1]-1, inverse(p[2]))
#                 if value not in colored_positions:
#                     colored_positions.add(value)
#                     grid[value[0]][value[1]] = value[2]
#             if (p[0], p[1]-1, p[2]) in colored_positions and (p[0], p[1]+1) in legal_positions:
#                 value = (p[0], p[1]+1, inverse(p[2]))
#                 if value not in colored_positions:
#                     colored_positions.add(value)
#                     grid[value[0]][value[1]] = value[2]
#             if (p[0]+1, p[1], p[2]) in colored_positions and (p[0]-1, p[1]) in legal_positions:
#                 value = (p[0]-1, p[1], inverse(p[2]))
#                 if value not in colored_positions:
#                     colored_positions.add(value)
#                     grid[value[0]][value[1]] = value[2]
#             if (p[0]-1, p[1], p[2]) in colored_positions and (p[0]+1, p[1]) in legal_positions:
#                 value = (p[0]+1, p[1], inverse(p[2]))
#                 if value not in colored_positions:
#                     colored_positions.add(value)
#                     grid[value[0]][value[1]] = value[2]
#
#
#             if (p[0], p[1] + 2, p[2]) in colored_positions:
#                 value = (p[0], p[1]+1, inverse(p[2]))
#                 if value not in colored_positions:
#                     colored_positions.add(value)
#                     grid[value[0]][value[1]] = value[2]
#
#             if (p[0]+2, p[1], p[2]) in colored_positions:
#                 value = (p[0]+1, p[1], inverse(p[2]))
#                 if value not in colored_positions:
#                     colored_positions.add(value)
#                     grid[value[0]][value[1]] = value[2]
#     # for position in colored_positions:
#     #     x, y, color = position
#     #     grid[x][y] = color
#     return ["".join(l) for l in grid]
#
# def inverse(colour):
#     colour_invert = {"W": "B",
#                        "B": "W"}
#     return colour_invert[colour]
#
# print(unruly(('......',
#         '..B...',
#         'W.B.W.',
#         '......',
#         'W...W.',
#         'WW..W.')))
#
# print(unruly(["B..........B",
#               "..BB.B.W..B.",
#               "B........B..",
#               "....BW.W...W",
#               ".W........W.",
#               ".W...B.....B",
#               "..B..BB...W.",
#               "BW....B....."]))