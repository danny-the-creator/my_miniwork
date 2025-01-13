# API - функционал, предоставляемый модулем или сервером
# API-ем сервера называется набор констант, функций и методов, которые мы можем использовать в своих целях, при этом про каждую из них известно, что она принимает,
                                        # что она возвращает, что она должна делать, но при этом мы можем не знать как реализована её техническая составляющая (как она это делает?)
                                                                                                                            # Нам это и не нужно чтобы успешно пользоваться модулем!
# OWM (предсказывает погоду)            !!! Но, без использования самой библиотеки owm
# import requests
#
# apiurl = 'https://api.openweathermap.org/data/2.5/weather'              # основная ссылка запроса
#
# params = {  'lat' : 25.197740628688468,
#             'lon' : 55.27322841192644,
#             'units' : 'metric',                                         # перевод из кельвина в цельсию
#             'appid' : '265149b85a7e21285e992960b1a681c8'}
#
# response = requests.get(apiurl, params=params)
# # print(response.headers)
# print(response.json())                          # json.load(response.text) аналогчная запись
# data = response.json()
# print(data['main']['temp'])                     # выводит текущую температуру

# !!! При работе с api сервера, чаще всего сервер предоставляет полную документацию своей работы (поэтому это первое место где стоит смотреть при возникновении вопроса или ошибки)


# First Program
# import requests
#
# # number = input()
# with open(r'C:\Users\danny\Downloads\dataset_24476_3.txt', 'r') as file:
#     text = file.read().split('\n')
#
#
#
# for number in text:
#     url = f'http://numbersapi.com/{number}/math?json=true'
#     res = requests.get(url)
#     data = res.json()
#
#     if data['found'] == True:
#         result = 'Interesting'
#     else:
#         result = 'Boring'
#     print(result)

# Final Program
# import requests
#
# client_id = '1a97f72b1a9bf8e0c891'
# client_secret = '81dae824ec65004946059bf6b1b0ccaf'
#
# response = requests.post("https://api.artsy.net/api/tokens/xapp_token",
#                   data={
#                       "client_id": client_id,
#                       "client_secret": client_secret
#                   })
# token = response.json()['token']
#
#
#
# with open(r'C:\Users\danny\Downloads\dataset_24476_4.txt', 'r') as file:
#     artists = file.read().split('\n')
# # print(artists)
# result = []
# for artist_id in artists:
#     url = f"https://api.artsy.net/api/artists/{artist_id}"
#     headers = {"X-Xapp-Token" : token}
#
#     res = requests.get(url, headers=headers)
#     res.encoding = 'utf-8'
#     name = res.json()['sortable_name']
#     birthday = res.json()['birthday']
#
#     list_of_artists = (name, birthday)
#
#     result.append(list_of_artists)
# result.sort(key=lambda x:(x[1], x[0]))
# # print(result)
# with open('file.txt', 'w', encoding='utf-8') as f:
#     for i in result:
#         name = i[0]
#         f.write(name+'\n')