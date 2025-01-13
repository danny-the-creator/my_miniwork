# numbers = {1, 2, 3, 12, 76, 12, 10, 42}               # Множество как и словарь задаётся в {...}      но порядок вывода чисел из множества не совпадает с порядком ввода
# numbers = set()                                               # Чтобы создать пустое множество нужно использовать set(), нельзя использовать пустые {}
# print(type(numbers))                                          # ! Множество это как список, но элементы не повторяются а также расположены в random порядке (no index!)
numbers = set([1, 1, 1, 3, 65, 73, 12, 3, 3, 2, 15, 12])    # Также множество можно задать превратив список или кортедж в множество, использую function set()
# print(numbers)

# print(65 in numbers)                # Проверка входит ли 65 в множество при помощи "...in..."   True/False
# numbers.add("Hi!")                  # set.add - Добавление элемента в множество      (set - множество)
# print(numbers)
# numbers.discard(65)                 # set.discard(element)/ set.remove(element) - удаляют элемент из множества
# numbers.remove(58)                  # Отличие в том, что при отсутсвии элемента в множестве remove() - выведет ошибку, а discard() - ничего не сделает
# print(numbers)
# numbers.pop()                       # set.pop() - удаляет первый элемент множества(, но так как множество имеет random sequence удалится random element)
# numbers.clear()                     # set.clear() - удаляет все элементы множества
# print(numbers)

numbers_1 = {"a", 1, 2, 3}
numbers_2 = {1, "a", "b", "c"}
# numbers_test = numbers_1.union(numbers_2)         # set_1.union(set_2) - объединение двух множеств
# numbers_test = numbers_1 | numbers_2              # "|" - выполняет точно такую же функцию
# numbers_test = numbers_1.intersection(numbers_2)    # Выводит пересечение множеств
# numbers_test = numbers_1 & numbers_2                # "&" - Тоже самое
# numbers_test = numbers_1 - numbers_2                # элементы которые есть в множестве №1 но не в множестве №2         (как в матеше)
# print(numbers_test)                              # Одинаковые элементы будут выведены только ОДИН раз (без повторения)

numbers_copy = numbers.copy()                   # set.copy() - копирует множество
# print(numbers)
# print(numbers_copy)
# print(len(numbers_copy))                    # len() - длина (количество) элементов в множестве (работает как и в списке, и в строке)

frozenset(numbers)                              # frozenset(set) - неизменяемое множество(нельзя добавить или удалить элементы)
# numbers_test = numbers_1 & frozenset(numbers_2)     # Но по прежему можно работать с самим множеством: объединять/ вычитать/ пересекать
# print(numbers_test)

# Aнонимные функции

# def rectangle_diogonal(a,b):              # Пример решения через обычную функцию
#     return (a**2 +b**2)**(0.5)            # Также нужен return()
# print(rectangle_diogonal(3,4))
# print((lambda a,b: (a**2 + b**2)**(0.5)) (3,4) )        # Тоже самое, только в одну строчку

lam = (lambda x, y: x if x < y else y) (123, 67)        # (lambda a, b: function)(a, b) - выполняется как def() с return, но не может превышать одну логическую строчку команд
# print(lam)                                                  # a, b - операнды, lambda можно использовать даже там где def() невозможен (к примеру в самом def())
                                                        # Определяются не в начале програмы, а прям на месте
