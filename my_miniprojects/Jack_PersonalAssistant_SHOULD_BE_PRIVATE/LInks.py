import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from colorama import Fore

# Подключение драйвера
chromedriver = r'D:\Программирование\Python начало\Jack_PersonalAssistant\Непрограммная часть\Драйвера\chromedriver.exe'
service = Service(chromedriver)

# GLOBALS
browser = None

def settings_for_googling(account = 1, incognito = 0, head = 1):
    '''Стандартные настройки'''
    options = webdriver.ChromeOptions()  # Объект дополнительных настроек
    options.add_argument("start-maximized")                         # Расскрывает в полноэкранном режиме

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'          # Мой стандартный Юзер_Агент
    options.add_argument(f'user-agent={user_agent}')                                            # Вход под прокси

    options.add_argument('--disable-blink-features=AutomationControlled')                       # Имитирует работу пользователя (гугл всё равно обнаруживает бота...)

    # Пользовательский аккаунт
    if account == 0:
        options.add_argument(r'--user-data-dir=D:\Программирование\Python начало\Jack_PersonalAssistant\Непрограммная часть\Не_трогать(костыль)\User Data') # Папка с аккаунтами
        options.add_argument('--profile-directory=Default')                     # Dark Lord
    elif account == 1:
        options.add_argument(r'--user-data-dir=D:\Программирование\Python начало\Jack_PersonalAssistant\Непрограммная часть\Не_трогать(костыль)\User Data')  # Папка с аккаунтами
        options.add_argument(r'--profile-directory=Profile 1')                  # Бадарев Данил
    # Аккаунты можно добавлять (сюда)
    else:
        options.add_argument(r'--incognito')

    # Incognito mod
    if incognito == 0:
        pass
    else:
        options.add_argument(r'--incognito')

    # Headless mod
    if head == 0:
        options.add_argument(r'--headless')
    else:
        pass
    return options

options = settings_for_googling()                                               # Изначально задаются стандартные настройки

def browser_for_googling(options=options):
    global browser
    browser = webdriver.Chrome(service=service, options=options)
    sleep(0.2)
    browser.get(r'https://yandex.ru/quasar/')

def browser_parsing(link, options=options):                                   # На будующее
    global browser
    options = settings_for_googling()
    browser = webdriver.Chrome(service=service, options=options)
    sleep(0.2)
    browser.get(link)
    return browser

def browser_quit():
    try:
        browser.close()
    except:
        pass
    browser.quit()
    # print('Код проработал')                 # \d

def decarator_quit(func):                                       # Декоратор для выхода из браузера (нигде не используется, но может пригодиться)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        finally:
            browser_quit()
        return result
    return wrapper

def new_window(link='https://www.google.com/'):
    if browser == None:
        browser_for_googling(options=options)
    if re.search(r'\bhttps://', link) == None:
        # link = f'https://yandex.ru/search/?lr=10313&text={link}'                              # Поиск в Яндексе
        link = f'https://www.google.com/search?q={link}'                                      # Поиск в Гугле
    try:
        sleep(0.2)
        browser.execute_script(f"window.open('{link}')")
    except Exception as ex:
        print('К сожалению не удалось открыть сайт...')
        print(f'{Fore.LIGHTRED_EX}{ex}{Fore.RESET}')


if __name__ == '__main__':
    options = settings_for_googling()
    try:
        while True:
            link = input('Введите запрос: ')
            if link in {'break', 'stop', 'quit', 'end', 'стоп'}:
                break
            new_window(link)
    finally:
        browser_quit()



