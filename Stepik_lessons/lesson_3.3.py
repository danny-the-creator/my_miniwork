# Почти любай url состоит из 3 основных частей: протокол -- домен -- путь до ресурса
#                                                https   stepik.org       512

# У протокола https есть свои методы, чаще всего используется метод GET (этот метод мы используем, когда переходим по ссылке и тд)
# Ещё один метод - POST (этот метод позволяет изменять информацию на странице, мы используем этот метод при регистрации, при транызакциях и тд)

# Запрос отправляется в текстовом формате (запрос != url, но инфа одна) и приходит тоже в текстовом формате (сначала информация о проведённом запросе, потом html код страницы)

# Чаще всего, для работы с html кодом не нужно знать теги, но некоторые из них важны, к примеру при работе с 'requests'

# <a.. href = url ссылка> .text. <\a>       # в html коде, при клике на текст, который заключён в тег <a>, мы перейдём по ссылке, указанной в href

# !!! requests                          # Библиотека, созданная для http запросов
import requests

# result = requests.get(url=r'https://stepik.org/lesson/24471/step/5?unit=6780')              # формируется и отправляется запрос, ответ записывается в переменную
# print(result.status_code)                                               # атрибуты нашего запроса, его status_code
# print(result.headers)                                                   # словарь, содержащий всю инфу о запросе, кроме самого html кода
# print(result.content)                                                   # бинарные данные (ничего не понятно)
# print(result.text)                              # можно использовать только с текстовыми ответами на наш запрос (кто бы мог подумать)

# result = requests.get(url=r'https://stepik.org/static/frontend/topbar_logo.svg')            # Поиск картинки
# print(result.status_code)
# print(result.headers['Content-Type'])                                   # Наш результат пришёл не в виде текста, а в виде изображения
# # print(result.text)                                                      # Попытка вывода текста, не даст ошибку, но результат вывода - полный бред
#
# with open('test_picture.svg', 'wb') as file:                            # таким образом можно сохранить картинку
#     file.write(result.content)

# В get запрос можно передавать свои параметры (естественно, которые поддерживает домен) в виде словаря с парами ключ - значения
# requests.get(url=..., params={key : value})

# Параметры можно передавать и подставлять в самом запросе, но атрибут 'params' позволяет сделать это намного легче и удобнее

# First Program
# import requests
# import re
#
# control = False
#
# first_link, second_link = input(), input()
#
# result = (requests.get(first_link)).text
#
# # links = re.findall('<a.*href="https://.+\.html"')
# links = re.findall('href="https://.+?\.html"', result)
# for link in links:
#     link = link[6:-1]
#     try:
#         temporary_result = (requests.get(link)).text
#     except:
#         pass
#     else:
#         temporary_links = re.findall('href="https://.+?\.html"', temporary_result)
#         for temporary_link in temporary_links:
#             temporary_link  = temporary_link[6:-1]
#             if temporary_link == second_link:
#                 print('Yes')
#                 control = True
#                 break
#         if control == True:
#             break
# if control == False:
#     print('No')


# !!! Final Program                     3.5 hours... for seven rows...          :(

# import re, requests
# html = requests.get(input()).text
# result_list = re.findall(r'(<a .*href=[\'"](\w+://)*([\w\.-]+)[/:\'"]?)', html)               # Здесь видна +- правильная работа со скобками в re
# result_list = {site[2] for site in result_list if bool(re.search('\w+', site[2]))}                    # для тех случаев, когда важна лишь часть результата
# result_list = list(result_list)
# result_list.sort()
# for site in result_list:
#     print(site)