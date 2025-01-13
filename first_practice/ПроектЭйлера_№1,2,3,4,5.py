# #1 +
# summ = 0
# for i in range(1000):
#     if (i % 3 == 0) or (i % 5 == 0):
#         summ+=i
# print(summ)


# #2 +
# summ = 2
# i = 0
# spisok = [1,2]
# while True:
#     n = spisok[-1] + spisok[-2]
#     if (summ + n) > 4000000:
#         break
#     spisok.append(n)
#     if n % 2 == 0:
#         summ += n
#     i += 1
# print(spisok)
# print(i)
# print(summ)

#3 - +?
# n = 600851475143
# spisok = []
# spisok_1 = []
# ii = 2
# while ii <= n**0.5:
#     ii += 1
#     if n % ii == 0:
#         spisok.append(ii)
# print(spisok)
# for i in spisok:
#     spisok_1.append(int(n / i))
# spisok = spisok + spisok_1
# for x in spisok:
#     j = 2
#     a = True
#     while a == True and j <= x**0.5:
#         if x % j == 0:
#             a = False
#         j+=1
#     if a == True:
#         result = x
# print(result)


# #4 +
# a = 0
# result = [0, 0, 0]
# for i in range(1000, 300, -1):
#     for j in range(1000, 100, -1):
#         if str(i*j)[::-1] == str(i*j)[:] and i*j > result[2]:
#             result = [i, j, i*j]
# print(result)


# #5 +?
# i = 20
# while True:
#     if i % 20 == 0 and i % 19 == 0 and i % 18 == 0 and i % 17 == 0 and i % 16 == 0\
#             and i % 15 == 0 and i % 14 == 0 and i % 13 == 0 and i % 12 == 0 and i % 11 == 0:
#         result = i
#         break
#     i += 20
# print(result)

# #Идеальный пример( не мой (работает в 2000 раз быстрее - НЕ ШУТКА!))
# def nod (a,b):
#     while b > 0:
#         a,b = b, a % b  # Формула НОД
#     return a
# def nok (a,b):
#     return a*b // nod(a,b) # Нок по формуле а*b // на нод a,b
# d = 1                              # В нем будет хранится значение предыдущего НОК
# for i in range (2,21):      # Перебераем делители
#     d = nok(d,i)                 # Ищем их НОК
# print (d)

