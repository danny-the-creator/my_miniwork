import pytz.exceptions
from pytz import timezone
import re
import datetime
def current_time(city = None, current = 'time', lang = 'ru'):
    time_ru_en = {'Monday' : 'Понедельник',
                 'Tuesday' : 'Вторник',
                 'Wensday' : 'Среда',
                 'Thursday' : 'Четверг',
                 'Friday' : 'Пятница',
                 'Saturday' : 'Суббота',
                 'Sunday':'Восскресенье',
                 'December' : 'Декабря',
                 'January' : 'Января',
                 'February' : 'Февраля',
                 'March' : 'Марта',
                 'April' : 'Апреля',
                 'May' : 'Мая',
                 'June' : 'Июня',
                 'July' : 'Июля',
                 'August' : 'Августа',
                 'September' : 'Сентября',
                 'October' : 'Октября',
                 'November' : 'Ноября'}
    Europe = ['Amsterdam', 'Andorra', 'Athens', 'Belgrade', 'Berlin', 'Bratislava', 'Brussels', 'Bucharest', 'Budapest', 'Chisinau',
              'Copenhagen', 'Dublin', 'Gibraltar', 'Guernsey', 'Helsinki', 'Isle_of_Man', 'Istanbul', 'Jersey', 'Kaliningrad', 'Kiev',
              'Lisbon', 'Ljubljana', 'London', 'Luxembourg', 'Madrid', 'Malta', 'Mariehamn', 'Minsk', 'Monaco', 'Moscow',
              'Nicosia', 'Oslo', 'Paris', 'Podgorica', 'Prague', 'Riga', 'Rome', 'Samara', 'San_Marino', 'Sarajevo',
              'Simferopol', 'Skopje', 'Sofia', 'Stockholm', 'Tallinn', 'Tirane', 'Uzhgorod', 'Vaduz', 'Vatican', 'Vienna',
              'Vilnius', 'Volgograd', 'Warsaw', 'Zagreb', 'Zaporozhye', 'Zurich']
    Asia  = ['Tokyo', 'Vladivostok', 'Yakutsk', 'Yekaterinburg', 'Tokyo', 'Riyadh' ]
    America = ['Nuuk', 'Lima', 'Juneau', 'Havana', 'Chicago', 'Costa_Rica', 'Los_Angeles', 'Montreal', 'New_York', 'Panama', 'Aruba']
    Else = { 'Cairo' : 'Africa/Cairo', 'Lusaka' : 'Africa/Lusaka', 'Brazil' : 'Brazil/East', 'Ottawa' : 'Canada/Eastern', 'Mexico' : 'America/Mexico_City',
             'Washington' : 'America/Aruba', 'Cape_Town' : 'Africa/Lusaka', 'Buenos_Aires' : 'America/Argentina/Buenos_Aires' }

    if city == None:
        zone = None
    elif city.capitalize() in Europe:
        zone = timezone(f'Europe/{city.capitalize()}')
    elif city.capitalize() in Asia:
        zone = timezone(f'Asia/{city.capitalize()}')
    elif city.capitalize() in America:
        zone = timezone(f'America/{city.capitalize()}')
    elif city.capitalize() in Else.keys():
        zone = timezone(Else[city.capitalize()])
    else:
        try:
            zone = timezone(city.capitalize())
        except pytz.UnknownTimeZoneError:
            if lang == 'ru':
                return 'Я не знаю такого места, если он вообще существует!'
            elif lang == 'en':
                return 'I don\'t know such a place!'

    time = datetime.datetime.now(tz = zone)
    Current_Time =  {'year' : time.year, 'month' : time.strftime('%B'), 'week' : time.strftime('%A'),
                     'day' : time.day, 'hour' : time.hour, 'minute' : time.minute}
    if current != 'time':
        return Current_Time[current]
    if lang == 'en':
        return f"{Current_Time['day']} {Current_Time['month']}, {Current_Time['week']}. \nCurrent Time: {Current_Time['hour']}:{Current_Time['minute']}"
    if lang == 'ru':
        return f"{Current_Time['day']}-ое {time_ru_en[Current_Time['month']]}, {time_ru_en[Current_Time['week']]}. \nТекущее Время: {Current_Time['hour']}:{Current_Time['minute']}"
previous_command = ''
if __name__ == '__main__':
    while True:
        command = input('Введите команду: ').lower()
        if command == 'время':
            print(current_time()[current_time().index('\n')+1:])
        elif command == 'дата':
            print(current_time())
        elif command == 'год':
            if previous_command == 'дата':
                print(f"{current_time(current='year')}, Путешественник")
            else:
                print(current_time(current='year'))
        elif command == 'число':
            print(current_time(current='day'))
        elif command == 'месяц':
            print(current_time(current='month'))
        elif command == 'день_недели':
            print(current_time(current='week'))
        elif command == 'только_час':
            print(current_time(current='hour'))
            print('Зачем?')
        elif command == 'минута':
            print(str(current_time(current='minute')) + '-ая')
            print('Нафига?')
        elif bool(re.search(r'секунда', command)) == True:
            print('Дофига точный?')
        else:
            print('Команда не из этого модуля!')
        previous_command = command
        print()
    # print(current_time(city='Moscow'))