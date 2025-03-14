
class Milk():                                               # class - как функция в которую можно вводить несколько функций (объекты имеющие схожие свойства и тд)
    """Описание свойств Молока одного производителя"""
    def __init__(self,storage_life,fatness):                # self - всегда занимает первую позицию, без неё программа не будет работать
        """Свойства Молока"""
        self.storage_life = storage_life                    # ввожу свойства объектов в классе
        self.fatness = fatness
        self.company = "Dan-dan-milk"                       # общее свойство всех объектов
    def warning(self):                                      # функция для класса, можно применить к любому объекту принадлежащему классу
        """Предупреждение об окончании срока годности"""
        print("Молоко с процентом жира " + str(self.fatness) + "% почти истекло, срок годности заканчивается: " + self.storage_life)
    def cooking(self,number):                               # функция с вводом доп инфы и её использованием
        """Советует что испечь из этого молока"""
        if self.fatness < 5:
            print("Из такого молока кашу не сваришь! Выпей его с печеньками!")
            print("Нужно " + str(int(float(number)/0.05)) + " печенья!")     # поскольку это доп инфа, которая не хранится в классе, она записывается без self.
        elif 5 < self.fatness <= 10:
            print("Пеки блины!")
            print("Можно испечь " + str(20*str(number)) + "блинов!")                                                                # self.number - неверно
        elif 10 < self.fatness <= 15:
            print("Советую сделать рулет!")
            print("Получится около " + str(12.5*int(number)) + "кг рулета, да у нас пир!")
        elif 15 < self.fatness < 25:
            print("Сделай Тирамису!")
            print("Тебе правда нужно " + str(3*int(number)) + "кг Тирамису?")
        else:
            print("Да это Масло! Скушай с хлебом!")
            print("Готовь "+ str(275*int(number)) + " бутербродов!")
Milk_1 = Milk("12.01.2022",10)                  # внос элемента в класс
Milk_2 = Milk("10.01.2022",20)
# print(Milk_1.storage_life)                    # вывод определённого свойства объекта
# print(Milk_2.fatness)
# Milk_1.warning()                              # Object.function(_)    -   использование определённой функции из класса (_) в скобки можно ввести доп параметры,
                                                                                                                            # если это нужно для работы конкретной функции
# print(Milk_1.company)
# Milk_2.cooking(2)

# class sour_milk(Milk):                          # устанавление связи Родитель- Потомок      (_) - Указан Родитель
#     """Описание свойств Сметаны другого производителя"""
#     def __init__(self,storage_life,megafatness):
#         """Свойства сметаны"""
#         super().__init__(self,storage_life)         # super() - Функция позволяющая взять свойство (или функцию от родителя) и передать потомку. !!! Нужно разобраться лучше!
#         self.megafatness = megafatness                      # также можно добавлять или изменять другие функции
# sour_milk_1 = sour_milk("17.09.2022", 35)
# print(sour_milk_1.storage_life)
# # print(sour_milk_1.megafatness)