# !!! Данный проект пока что представляет из себя лишь идею. Он НЕ завершён
# < Заморожен >

import re
import time
class Milk_product():
    """Описание свойств Молока одного производителя"""
    def __init__(self,spoiled_date,fatness):
        """Свойства Молока"""
        self.spoiled_date = spoiled_date
        self.fatness = fatness
        self.company = "Dan-dan-milk"
    def storage_life(self):
        """Предупреждение об окончании срока годности"""
        spoiled_date = self.spoiled_date.split(".")
        today_date = time.strftime('%d.%m.%Y')
        today_day = time.strftime('%d')
        today_month = time.strftime('%m')
        today_year = time.strftime('%Y')
        dictanory = {"01" : 0, "02" : 31, "03" : 59, "04" : 90, "05" : 120, "06" : 151,\
                     "07" : 181, "08" : 212, "09" : 243, "10" : 273, "11" : 304, "12" : 334,}       # Дни от начала года в зависимости от месяца
        if spoiled_date[2] > today_year:
            answer = "Не парься, у выбранного продукта больше года срока годности!"
        elif spoiled_date[2] < today_year:
            answer = "Ух, да этот продукт испортился больше года назад, выкинь эту дрянь!"
        else:
            if int(today_year) % 4 == 0 and (int(spoiled_date[1]) > 2) and (int(today_month) <= 2):
                result = (dictanory[spoiled_date[1]] + int(spoiled_date[0]) + 1) - (dictanory[today_month] + int(today_day))
            elif int(today_year) % 4 == 0 and (int(spoiled_date[1]) <= 2) and (int(today_month) > 2):
                result = (dictanory[spoiled_date[1]] + int(spoiled_date[0]) ) - (dictanory[today_month] + int(today_day) + 1)
            else:
                result = (dictanory[spoiled_date[1]] + int(spoiled_date[0])) - (dictanory[today_month] + int(today_day))
            if result == 0:
                answer = "Этот продукт испортится СЕГОДНЯ! Тебе нужно скорее придумать, что с ним делать!"
            elif -4 <= result < 0:
                answer = "Этот продукт уже не свежий, советую использовать где-то в готовке!"
            elif result < -4:
                answer = "Этот продукт ИСПОРТИЛСЯ {} дней назад, советую его ВЫКИНУТЬ!".format(-result)
            else:
                answer = "Этот продукт испортится через {} дней".format(result)
        print(answer)

Milk = Milk_product("18.04.2022", 5)
SourMilk = Milk_product("30.04.2022", 20)
Chefir = Milk_product("25.04.2022", 15)
# Chefir.storage_life()