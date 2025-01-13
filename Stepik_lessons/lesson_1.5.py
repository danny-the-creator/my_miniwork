# В каждом классе (созданным или уже существующим в Python) есть свой 'конструктор класса'
# Он вызывается при помощи '()' после названия класса [str(), list()]

# x = str()                               # Это явная задача класса string
# print(type(x))                                      # Мы создали объект класса при помощи конструктора класса 'str'
#
# print('' == x)                          # [''] - это способ неявного создания объекта класса (тоже самое)

# !!! Когда мы пытаемся изменить класс объекта, мы его не меняем напрямую, мы удаляем объект прошлого класса и присваеваем этому объекту новый класс4
                                                                                # (Да, звучит очевидно, однако ты не задумываешься над этим в момент использования классов)

# У каждого объекта класса есть своё пространство имён (туда мы можем вносить новые имена в ходе выполнения программы)

# class Counter:
#     pass                                        # Пустой класс, который ничего не делает (однако мы по прежнему можем использовать конструктор класса)
#
# x = Counter()                                   # 'x' -  является экземпляром класса Counter
# x.count = 0                                     # Мы создали в пространстве имён x имя count (которому присвоили значение 0)
# x.count += 1                                    # Мы можем с лёгкостью влиять на этот объект (count) экземпляра класса Counter (x)
# print(x.count)

# class Counter:
#     def __init__(self):             # __init__ нужен для того чтобы при создании НОВОГО ЭКЗЕМПЛЯРА КЛАССА он обладал стандартныс набором характеристик
#         self.count = 0              # self - это сам объект класса, который будет создан (Поскольку Python автоматически подставляет ОБЪЕКТ экземпляра класса вместо self
#                                                                                     # для нас этот аргумент становится невидим, но НЕЛЬЗЯ забывать об его существовании )
# x = Counter()                       # в данном случае в функции __init__ вместо self подставляется 'x'
# y = Counter()                       # в данном случае в функции __init__ вместо self подставляется 'x'

# Запись сверху равносильна следующей записи
# class Counter:
#     def __init__(self):
#         self.count = 0
# x = Counter()
# y = Counter()
# x.count = 0
# y.count = 0                             # И так нужно будет добавлять для каждого нового экземпляра класса

# !!! А вообще функция __init__ нужна только для конструктора (чтобы настраивать стартовые данные для каждого нового экземпляра класса)

# Метод класса это ФУНКЦИЯ внутри КЛАССА предназначенная ТОЛЬКО для этого класса
# В каждом методе тоже должен присутствовать аргумент 'self', вместо которого будет подставляться объект экземпляра класса

# class Counter:
#     def __init__(self):
#         self.count = 0
#     def inc(self):
#         self.count += 1
# x = Counter()
# x.inc()                                 # Эта запись равносильна следующей записи (тоxнее так её понимает сам питон и по такому же принципу выполняет её) -->
# Counter.inc(x)
# print(x.count)

# Program
class MoneyBox:
    def __init__(self, capacity):
        self.quantity = 0
        self.capacity = capacity

    def can_add(self, v):
        return  self.quantity + v <= self.capacity

    def add(self, v):
        self.quantity += v

x = MoneyBox(15)
x.add(5)
x.add(9)
# print(x.can_add(1))

# Final Program
class Buffer:
    def __init__(self):
        self.list = []

    def add(self, *args):
        self.list += args
        while len(self.list) >= 5:
            print(sum(self.list[:5]))
            self.list = self.list[5:]

    def get_current_part(self):
        return self.list

