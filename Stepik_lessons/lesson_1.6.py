# Наследование классов
class MYlist(list):                             # После имени самого класса указываются его 'родителИ' в скобках, это те самые классы от которых мы будем всё наследовать
    pass                                        # Даже если закончить описание класса на этом моменте, он уже будет обладать всеми методами и возможностями класса list
    def revers(self):                           # Эта функция выводит перевёрнутый список
        return self[::-1]

# x = MYlist()
# print(x)
# x.extend([1, 2, 3])                     # Поиск атрибутов будет происходить следующим образом: сначала мы будем искать в экземпляре класса (x), потом в самом классе
# print(x)                                                                                                        # и только потом во всех классах, которые мы наследовали
# print(x.revers())

# !!! так как поиск происходит в порядке приведённом выше, мы встретим метод класса раньше, чем метод его родителя, тоесть

# class MYstr(str):
#     def upper(self):
#         print('мне лень, сам поднимай')
# x = MYstr('fff')
# x.upper()                                   # в данном случае стандартная функция 'upper' была заменена на нашу, без удаления таковой в 'родителе' класса (str)

print(issubclass(MYlist, list))                 # выводит является ли первый введённый класс наследником второго класса (возвращает Trye/False)
print(issubclass(list, MYlist))
print(issubclass(MYlist, MYlist))               # ! Любой класс является наследником самого себя
print(issubclass(list, object))                 # ! Любой класс является наследником класса object (object - предок всех предков) (object - не может быть наследником)

# !!! существует похожий метод isinstance
isinstance(x, list)                             # Делает тоже самое, только проверяет всё тоже самое для экземпляров класса

MYlist.mro()                                    # Возвращает путь по которому будет происходить поиск метода класса (полезно когда наследуюешь несколько классов,
                                                                                                                        # которые в свою очередь являются наследниками)

# Hard Test
# inheritance = {}
#
# def inherit(son, parent):
#     global inheritance
#     if inheritance.get(son) == None:
#         inheritance[son] = []
#     if parent in inheritance[son] or son == parent:
#         return 'Yes'
#     for i in inheritance[son]:
#         if inherit(son=i, parent=parent) == 'Yes':
#             return 'Yes'
#
# for i in range(int(input())):
#     command = input()
#     if ':' in command:
#         son, parent = command.split(' : ')
#         inheritance[son] = parent.split()
#     else:
#         inheritance[command] = []
# # print( inheritance)
#
# for i in range(int(input())):
#     parent, son = input().split()
#     result = inherit(son=son, parent=parent)
#     if result == None:
#         print('No')
#     else:
#         print('Yes')

# Test #2
class ExtendedStack(list):
    def sum(self):
        self.append(self.pop() + self.pop())

    def sub(self):
        self.append(self.pop() - self.pop())

    def mul(self):
        self.append(self.pop() * self.pop())

    def div(self):
        self.append(self.pop() // self.pop())

# Final Test
class  LoggableList(list):
    def append(self, number):
        list.append(self, number)
        print(number)

x = LoggableList()
x.append(5)
print(x)