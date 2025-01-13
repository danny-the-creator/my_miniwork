def unruly(grid):
    grid = [list(s) for s in grid]
    legal_positions = [(i, j) for i in range(len(grid)) for j in range(len(grid[i]))]
    colored_positions = {(i, j, grid[i][j]) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] != '.'}
    rows = {r: {"B": 0, "W": 0} for r in range(len(grid))}
    cols = {c: {"B": 0, "W": 0} for c in range(len(grid[0]))}
    while len(colored_positions) < (len(grid) + 1) * (len(grid[0]) + 1):

        print(len(colored_positions))
        for row, v in rows.items():
            if v["B"] == len(grid) / 2:
                for col in range(len(grid[0])):
                    value = (row, col, "W")
                    if value not in colored_positions and (row, col, "B") not in colored_positions:
                        colored_positions.add(value)
                        cols[col]["W"] += 1
                # rows.pop(row)
            if v["W"] == len(grid[0]) / 2:
                for col in range(len(grid[0])):
                    value = (row, col, "B")
                    if value not in colored_positions and (row, col, "W") not in colored_positions:
                        colored_positions.add(value)
                        cols[col]["B"] += 1
                # rows.pop(row)
        for col, v in cols.items():
            if v["B"] == 4:
                for row in range(len(grid)):
                    value = (row, col, "W")
                    if value not in colored_positions and (row, col, "B") not in colored_positions:
                        colored_positions.add(value)
                        rows[row]["W"] += 1
                # cols.pop(col)
            if v["W"] == 4:
                for row in range(len(grid)):
                    value = (row, col, "B")
                    if value not in colored_positions and (row, col, "W") not in colored_positions:
                        colored_positions.add(value)
                        rows[row]["B"] += 1
                # cols.pop(col)

        for p in colored_positions.copy():
            if (p[0], p[1] + 1, p[2]) in colored_positions and (p[0], p[1] - 1) in legal_positions:
                value = (p[0], p[1] - 1, inverse(p[2]))
                if value not in colored_positions:
                    colored_positions.add(value)
                    rows[value[0]][value[2]] += 1
                    cols[value[1]][value[2]] += 1
                    grid[value[0]][value[1]] = value[2]
            if (p[0], p[1] - 1, p[2]) in colored_positions and (p[0], p[1] + 1) in legal_positions:
                value = (p[0], p[1] + 1, inverse(p[2]))
                if value not in colored_positions:
                    colored_positions.add(value)
                    rows[value[0]][value[2]] += 1
                    cols[value[1]][value[2]] += 1
                    grid[value[0]][value[1]] = value[2]
            if (p[0] + 1, p[1], p[2]) in colored_positions and (p[0] - 1, p[1]) in legal_positions:
                value = (p[0] - 1, p[1], inverse(p[2]))
                if value not in colored_positions:
                    colored_positions.add(value)
                    rows[value[0]][value[2]] += 1
                    cols[value[1]][value[2]] += 1
                    grid[value[0]][value[1]] = value[2]
            if (p[0] - 1, p[1], p[2]) in colored_positions and (p[0] + 1, p[1]) in legal_positions:
                value = (p[0] + 1, p[1], inverse(p[2]))
                if value not in colored_positions:
                    colored_positions.add(value)
                    rows[value[0]][value[2]] += 1
                    cols[value[1]][value[2]] += 1
                    grid[value[0]][value[1]] = value[2]

            if (p[0], p[1] + 2, p[2]) in colored_positions:
                value = (p[0], p[1] + 1, inverse(p[2]))
                if value not in colored_positions:
                    colored_positions.add(value)
                    rows[value[0]][value[2]] += 1
                    cols[value[1]][value[2]] += 1
                    grid[value[0]][value[1]] = value[2]

            if (p[0] + 2, p[1], p[2]) in colored_positions:
                value = (p[0] + 1, p[1], inverse(p[2]))
                if value not in colored_positions:
                    colored_positions.add(value)
                    rows[value[0]][value[2]] += 1
                    cols[value[1]][value[2]] += 1
                    grid[value[0]][value[1]] = value[2]
    for position in colored_positions:
        x, y, color = position
        grid[x][y] = color
    return ["".join(l) for l in grid]


def inverse(colour):
    colour_invert = {"W": "B",
                     "B": "W"}
    return colour_invert[colour]


print(unruly(('......',
              '..B...',
              'W.B.W.',
              '......',
              'W...W.',
              'WW..W.')))