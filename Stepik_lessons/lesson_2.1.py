# Ошибки делятся на два типа: Syntax errors (чаще всего опечатки или забытые знаки [:,()]) и все остальные (несуществующая переменная, деление на 0 ...)
# Если в файле есть хоть одна Syntax error, интерпретатор даже не запустится, даже если он может выполнить код до ошибки

# ! В блоке 'try' может быть больше одного 'except'

# Ошибки имеют свою иерархию и наследуются от других ошибок (Однако, у каждой ошибки может быть только один предок!)
# print(ZeroDivisionError.mro())          # [<class 'ZeroDivisionError'>, <class 'ArithmeticError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>]

# Именно по этой иерархии блоке except будет ловить ошибки (тоесть, елси мы будем ловить BaseException, мы сможем поймать и всех её наследников )

# Program
# try:
#     foo()
# except ZeroDivisionError as ex:
#     print('ZeroDivisionError')
# except ArithmeticError as ex:
#     print('ArithmeticError')
# except AssertionError as ex:
#     print('AssertionError')

# Govno Program

# ErrorsFamily = {}
# UseControl = []
#
# def recursia(command):
#     if ErrorsFamily.get(command) == None:
#         ErrorsFamily[command] == []
#     for i in ErrorsFamily[command]:
#         if i in UseControl:
#             return command
#         result = recursia(i)
#         if result != None:
#             return result
#
# for i in range(int(input())):
#     command = input()
#     if ':' in command:
#         son, parent = command.split(' : ')
#         ErrorsFamily[son] = parent.split()
#     else:
#         ErrorsFamily[command] = []
#
# print(ErrorsFamily)
#
# for i in range(int(input())):
#     command = input()
#     if recursia(command) != None:
#         print(command)
#     UseControl.append(command)

class Error404(Exception):              # таким образом можно создавать свои собственные ошибки
    pass
# raise  Error404('Самоуничтожение через ...')            # А так можно 'бросить' свою ошибку

# Final Program
class NonPositiveError(Exception):
    pass
class PositiveList(list):
    def append(self, __object):
        if __object <= 0:
            raise NonPositiveError
        list.append(self, __object)