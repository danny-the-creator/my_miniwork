import re
from time import sleep
import datetime

def timer(time, func = lambda : print('Время Вышло!'), lang = 'ru'):
    # if lang != 'ru':                                                                              # Пока что не работает
    #     translate(time, into = 'ru')
    time = time.replace(' и', '').lower()
    time = time.replace('один', '1').replace('одну', '1').replace('одна', '1')

    minhour = re.search(r'\d{1,2}:\d{1,2}', time)
    if minhour != None:
        time = time.replace(minhour[0], '')
        minhour = minhour[0].split(':')
        hours = minhour[0]
        minutes = minhour[1]
    else:
        hours = re.search(r'\d{1,2} час\w{0,8}|час\w{0,8} \d{1,2}', time)
        if hours != None:
            time = time.replace(hours[0], '')
            hours = re.search(r'\d{1,2}', hours[0])[0]
        else:
            hours = 0
        minutes = re.search(r'\d{1,3} мин\w{0,8}|мин\w{0,8} \d{1,3}', time)
        if minutes != None:
            time = time.replace(minutes[0], '')
            minutes = re.search(r'\d{1,3}', minutes[0])[0]
        else:
            minutes = 0

    seconds = re.search(r'\d{1,5} сек\w{0,8}|сек\w{0,8} \d{1,5}', time)
    if seconds != None:
        time = time.replace(seconds[0], '')
        seconds = re.search(r'\d{1,5}', seconds[0])[0]
    else:
        all_numbers = re.findall(r'\d+', time)
        if len(all_numbers) == 1:
            seconds = all_numbers[0]
            time = time.replace(seconds, '')
        else:
            seconds = 0

    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)

    # print(time)  # d
    if seconds == minutes == hours == 0 or re.search(r'сек\w{0,8}|мин\w{0,8}|час\w{0,8}', time):
        print('К сожалению, у нас возникло недопонимание\nПрошу понять, простить и ПОВТОРИТЬ ЗАПРОС!')
        return ''

    when = f'Таймер сработает через: {hours} часов {minutes} минут {seconds} секунд'
    when = when.replace('1 часов', '1 час').replace('1 минут', '1 минуту').replace('1 секунд', '1 секунду')
    when = when.replace('11 час', '11 часов').replace('11 минуту', '11 минут').replace('11 секунду', '11 секунд')                   # Нужно после первой замены
    when = re.sub(r'\b0 \w+', '', when)
    when = re.sub(r'\b[23456789]?[234] часов', f'{hours} часа', when)                                 # '?' == {0,1}
    when = re.sub(r'\b[23456789]?[234] минут', f'{minutes} минуты', when)                             # Можно будет добавить правильную запись (не 10 минут и 330 секунд,
    when = re.sub(r'\b[23456789]?[234] секунд', f'{seconds} секунды', when)                                                                         # а 15 минут и 30 секунд)
    print(when)

    time = hours*3600 + minutes*60 + seconds
    # print(time)                                         # d

    sleep(time)
    func()

start = 'Stop'                                  # Если не будет работать можно добавить     < stopwatch_paused = '' >
def stopwatch(command = 'time', lang = 'ru'):
    # if lang != 'ru':                                                                              # Пока что не работает
    #     translate(time, into = 'ru')
    global start, stopwatch_paused
    if command == 'time':
        if start == 'Stop':
            result = 'Секундомер не включен!'
        elif start == 'Pause':
            result = str(stopwatch_paused)[:-4]                                       # Выводит только десятые и сотые секунды
            result = re.sub(r'\b0:', '', result)                                            # Если прошло меньше часа, то часы не будут выводиться
        else:
            result = str(datetime.datetime.now() - start)[:-4]                        # Выводит только десятые и сотые секунды
            result = re.sub(r'\b0:', '', result)                                            # Если прошло меньше часа, то часы не будут выводиться
    elif command == 'start':
        start = datetime.datetime.now()
        result = 'Запустил секундамер'
    elif command == 'stop':
        start = 'Stop'
        result = 'Сбросил секундамер'
    elif command == 'pause':
        if start == 'Pause':
            result = 'Секундомер и так на паузе'
        elif start == 'Stop':
            result = 'Секундомер ещё не запущен!'
        else:
            stopwatch_paused = datetime.datetime.now() - start
            start = 'Pause'
            result = 'Поставил секундомер на паузу'
    elif command == 'unpause':
        if start == 'Pause':
            start = datetime.datetime.now() - stopwatch_paused
        result = 'Возобновил секундомер' if start != 'Stop' else 'Секундомер ещё не запущен!'
    else:
        result = 'Данная команда не присутствует в этом модуле!'

    return result


if __name__ == '__main__':
    # timer(time='12 часов 10 минут и 330 секунд' )

    # timer('0:0:5', lambda : exec("test('Привет мир!', 'Хороший день!', 3)"))          # другой вариант                exec - выполняет заданный кусок кода
    # timer('0:0:5', lambda : test('Привет мир!', 'Хороший день!', 3))

    while True:
        command = input('Введите команду: ')
        if command == 'exit' or command == 'end':
            print('Завершаю программу')
            break
        print(stopwatch(command))
        print()
