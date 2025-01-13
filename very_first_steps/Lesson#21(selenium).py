# Модуль 'selenium' используется для открытия сайтов в браузере и для парсинга

import selenium
from selenium.webdriver.chrome.service import Service
from time import sleep
from colorama import Fore
import pickle

chromedriver = r'D:\Программирование\Python начало\Jack_PersonalAssistant\Непрограммная часть\Драйвера\chromedriver.exe'
service = Service(chromedriver)

options = selenium.webdriver.ChromeOptions()
options.add_argument("start-maximized")

options.add_argument(r'--user-data-dir=D:\Программирование\Python начало\Jack_PersonalAssistant\Непрограммная часть\Не_трогать(костыль)\User Data') # Входит в аккаунт (в копию)

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'          # Прокси

options.add_argument(f'user-agent={user_agent}')                                                                                        # Вход под прокси

options.add_argument('--disable-blink-features=AutomationControlled')             # Имитирует работу пользователя

# Профили
# options.add_argument('--profile-directory=Default')                               # Dark Lord
options.add_argument(r'--profile-directory=Profile 1')                             # Бадарев Данил

options.add_argument(r'--incognito')                                                # Incognito

# options.add_argument(r'--headless')                                                 # Запуск браузера в фоновом режиме

link = r'https://yandex.ru/quasar/'
links = [r'https://www.mamba.ru/ru', r'https://loveplanet.ru/', r'https://loveplanet.ru/', r'https://badoo.com/', r'https://love.ru/', r'https://dating.ru/', r'https://love.ru/',
         r'https://www.youtube.com/watch?v=hwEpNd6Yles&ab_channel=TheHeatRush', r'https://fotostrana.ru/', r'https://tabor.ru/', r'https://love.ru/', r'https://www.maybe.ru/']

# Создание ОБЪЕКТА браузера
browser = selenium.webdriver.Chrome(service=service, options=options)


# Cookies
# После открытия сайта можно сохранить 'cookies', вот так:
#             pickle.dump(browser.get_cookies(), open(r'D:path...\cookies', 'wb'))

# После сохранения 'cookies' в другой программе или при следующем входе, можно будет просто подгрузить 'cookies'
#         тем самым избежав Повторного Вода Данных (учётная запись, имя, пароли...)
#                   Подгрузить 'cookies' можно следующим образом:
#                             for cookie in pickle.load(open(r'D:path...\cookies', 'rb')):
#                                 browser.add_cookie(cookie)
#   После чего дастаточно просто перезагрузить страницу следующим образом: browser.refresh()
#                                                                   Желательно перед перезагрузкой сделать небольшую паузу (sleep(3))


# Гуглим
try:
    sleep(0.2)
    browser.get(url=link)
    for link in links:
        try:
            sleep(0.2)
            browser.execute_script(f"window.open('{link}')")
            sleep(3)
            # input()
        except Exception as ex:
            # print('У вас Ошибка')
            # print(f'{Fore.LIGHTRED_EX}{ex}{Fore.RESET}')
            break
finally:
    try:
        browser.close()
    except:
        pass
    browser.quit()
    print('Код проработал')