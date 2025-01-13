limit = 1000000

spisok = [2,3]
for i in range(5,limit, 2):
    j = 3
    control = True
    while j <= i ** 0.5:
        if i % j == 0:
            control = False
        j += 1
    if control == True:
        spisok.append(i)

all_numbers = set(spisok)

max = 0
result = 0
a = -1
for q in spisok[::-1]:
    n = 0
    summ = 0
    a -= 1
    j = a
    if -j < len(spisok):
        while summ + spisok[j] <= limit:
            summ += spisok[j]
            n += 1
            j -= 1
            if -1*j > len(spisok):
                break
            if max < n and summ in all_numbers:
                max = n
                result = summ
print(result)                                   # result = 997651
print(max)                                      # max = 543