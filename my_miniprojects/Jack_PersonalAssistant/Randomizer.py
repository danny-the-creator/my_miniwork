import re
from colorama import Fore
import random

def space_deleter(text):
    """Cоздаёт список из введённого предложения, разбивая его по пробелам, но игнорируя множественные пробелы"""
    split = text.split(' ')
    return " ".join([i for i in split if len(i) != 0])

# !!! Можно добавить звуки !!!

def dice():
    '''Подкидывает Кубик'''
    return f'Выпало {Fore.LIGHTYELLOW_EX}{random.randint(1, 6)}{Fore.RESET}'
def coin():
    '''Подкидывает Монетку'''
    choice = random.random() - 0.5
    if choice > 0:
        return f'Выпал {Fore.LIGHTYELLOW_EX}Орёл{Fore.RESET}'
    elif choice < 0:
        return f'Выпала {Fore.LIGHTYELLOW_EX}Решка{Fore.RESET}'
    else:
        return f'Сэр, скорее берите лотерейный билет!\nУ нас {Fore.LIGHTYELLOW_EX}РЕБРО !!!{Fore.RESET}'

def choice(list):
    '''Выбирает Случайный Элемент Из Списка'''
    return f'Я выбираю... {Fore.LIGHTYELLOW_EX}{random.choice(list)}{Fore.RESET}'
def random_number(text='от 0 до 100'):                              # Ненужные слова в команде будут уберать до этого
    '''Генерирует любой номер от и до'''
    text = space_deleter(text.lower())
    if re.search(r'до -\d+|до \d+', text) == None:
        return 'Неправильно задан вопрос!\nПовторите ещё раз!'
    if re.search(r'\d+[.,/]\d+', text):
        return 'Дробные числа не поддерживаются!\nПовторите запрос!'
    From = re.search(r'от -\d+|от \d+', text)
    To = re.search(r'до -\d+|до \d+', text)
    To = int(re.search('-\d+|\d+' , To[0])[0])                           # Отделяем число от строки 'до '
    if From == None:
        From = 0
    else:
        From = int(re.search('-\d+|\d+' , From[0])[0])                   # Отделяем число от строки 'от '
    try:
        result = random.randint(From, To)
    except ValueError:
        result = random.randint(To, From)
    return f'{Fore.LIGHTYELLOW_EX}{result}{Fore.RESET}'



if __name__ == '__main__':
    print(dice())
    print(coin())
    print(choice(['fear', 'misery', 'insanity', 'madness', 'pain', 'death']))
    print(random_number('rtyui ОТ 3005      до   -3000'))
