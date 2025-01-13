def spin(length):                           # создаёт квадрат с заданными сторонами и выводит числа в нём по спирале
    square = [['_' for j in range(length)] for i in range(length)]
    number = 1
    i = 0
    while number<=length**2:
        for n in range(4):
            for j in range(length):
                if square[i][j] != '_':
                    continue
                square[i][j] = number
                number+=1
            square = [[square[j][i] for j in range(length)] for i in range(length)][::-1]       # поворот квадрата на 90
        i+=1
    return square
print(spin(5))
