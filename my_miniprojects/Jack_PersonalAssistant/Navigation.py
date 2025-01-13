import requests
from time import sleep
from geopy.geocoders import Nominatim
from colorama import Fore
from LInks import browser_parsing, browser_quit
import folium
import pickle

# Coordinates

# GLOBAL
    # Для генерации html карты с метками: их добавление и удаление
homeland_coordinates = [47.0316, 28.8620]
myLocation = [40.676762, 24.521355]                          # Заглушка
WorldMap = None



def StartMapGeneration():
    global WorldMap, MapHistory

    IconMods = {0: None,
                1: folium.Icon(icon='heart', color='red'),
                2: folium.Icon(icon='info-sign', color='orange'),
                3: folium.Icon(icon='camera', color='beige')}

    WorldMap = folium.Map(location=myLocation, zoom_start=15, max_bounds=True, min_zoom=3)
    WorldMap.add_child(folium.LatLngPopup())                                            # Показывает координаты, при клике на любое место карты

    # Показывает на карте ваше текущее местоположение
    myLocation_icon = folium.features.CustomIcon(r'D:\Программирование\Python начало\Jack_PersonalAssistant\Непрограммная часть\Звуки_и_фото\My_location.png', icon_size=(20, 20))
    folium.Marker(myLocation, popup=f'<i>{myLocation[0]}, {myLocation[1]}</i>', tooltip='<b>Your Coordinates</b>',icon=myLocation_icon).add_to(WorldMap)

    # Можно указать местоположение вашей текущей базы
    folium.Marker(homeland_coordinates, popup='Владимереску 1/4', tooltip='<b>Home</b>', icon=folium.Icon(icon='home', color='green')).add_to(WorldMap)

    with open('D:\Программирование\Python начало\Jack_PersonalAssistant\Непрограммная часть\Не_трогать(костыль)\MapInfo.pickle', 'rb') as file:
        MapHistory = pickle.load(file)                                                      # MapHistory хранит в себе историю всех созданных до этого маркеров в списке
                                                                                                        # Каждый элемент этого списка имеет вид: "(coords, name, icon_mode)"
                                                                                                                    # coords == [lat, lon]
    for marker in MapHistory:
        folium.Marker(location=marker[0], popup=f'<i>{marker[0][0]}, {marker[0][1]}</i>', tooltip=f'<b>{marker[1]}</b>', icon=IconMods[marker[2]]).add_to(WorldMap)

    WorldMap.save(r'D:\Программирование\Python начало\Jack_PersonalAssistant\Непрограммная часть\_!_Используемая_инфа\carta.html')


def add_location(coords, name='New Location', icon_mode=0):
    global WorldMap, MapHistory
    try:
        if type(coords) not in (list, tuple) or len(coords) != 2 or int(coords[0]) not in range(-180, 180) or int(coords[1]) not in range(-180, 180):
            int('Costil')
    except ValueError:
        print(f'{Fore.RED}Координаты введены неверно!{Fore.RESET}')
        return

    coords = [round(i, 5) for i in coords]

    IconMods = {0 : None,
                1 : folium.Icon(icon='heart', color='red'),
                2 : folium.Icon(icon='info-sign', color='orange'),
                3 : folium.Icon(icon='camera', color='beige')}

    if WorldMap == None:
        StartMapGeneration()

    folium.Marker(location=coords, popup=f'<i>{coords[0]}, {coords[1]}</i>', tooltip=f'<b>{name}</b>', icon=IconMods.get(icon_mode)).add_to(WorldMap)

    MapHistory.append((coords, name, icon_mode))

    # Сохраняем историю всех маркеров
    with open('D:\Программирование\Python начало\Jack_PersonalAssistant\Непрограммная часть\Не_трогать(костыль)\MapInfo.pickle', 'wb') as file:
        pickle.dump(MapHistory, file)
    # Сохраняем саму карту в html файл
    WorldMap.save(r'D:\Программирование\Python начало\Jack_PersonalAssistant\Непрограммная часть\_!_Используемая_инфа\carta.html')


def delete_location():
    with open('D:\Программирование\Python начало\Jack_PersonalAssistant\Непрограммная часть\Не_трогать(костыль)\MapInfo.pickle','rb') as file:
        MapHistory = pickle.load(file)

    if len(MapHistory) == 0:
        print('Оставшиеся метки нельзя убрать (их можно изменить в коде)')
        return 'Оставшиеся метки нельзя убрать!'
    MapHistory.pop()                                # удаляем данные о последней метке
    with open('D:\Программирование\Python начало\Jack_PersonalAssistant\Непрограммная часть\Не_трогать(костыль)\MapInfo.pickle', 'wb') as file:
        pickle.dump(MapHistory, file)

    StartMapGeneration()
    print('Удалил')
    return ('Удалил')


def get_ip_info(key='ip', ip=''):
    '''Возвращает данные из ip устройства (неточные данные)'''
    try:
        ip_information = requests.get(f'http://ip-api.com/json/{ip}').json() # выводит информацию по ip (если ip не указан, то выдаются данный по ip устройства (моему ip))
    except requests.exceptions.ConnectionError:
        return f'{Fore.LIGHTRED_EX}ERROR{Fore.RESET}: Something wrong with your conection!'
    key = key.lower().replace('ip', 'query').replace('internet_provider', 'isp')        # позволяет чаще воспринимать ключи
    result = ip_information.get(key)
    return result if result != None else 'Нет такой характеристики'

def get_coordinates(place):
    '''Возвращает координаты введённого адреса'''
    geo_driver = Nominatim(user_agent='user007')
    try:
        location = geo_driver.geocode(place).raw
    except AttributeError:
        return f'Место находится за пределами этой планеты, или вы просто {Fore.LIGHTRED_EX}Неправильно Ввели Адрес{Fore.RESET}!'
    return (location['lat'], location['lon'])

def way_to(st_lat, st_lon, fin_lat, fin_lon):
    browser_parsing(link=f'https://www.google.com/maps/dir/{st_lat},{st_lon}/{fin_lat},{fin_lon}/@{st_lat},{st_lon},15z')


def add_location(coords, name='New Location', icon_mode=0):
    global m
    try:
        if type(coords) not in (list, tuple) or len(coords) != 2 or int(coords[0]) not in range(-180, 180) or int(coords[1]) not in range(-180, 180):
            int('Costil')
    except ValueError:
        print(f'{Fore.RED}Координаты введены неверно!{Fore.RESET}')
        return

    coords = [round(i, 5) for i in coords]          # ? (не было проверки (должно работать))

    if icon_mode == 0:
        icon_mode = None
    elif icon_mode == 1:
        icon_mode = folium.Icon(icon='heart', color='red')
    elif icon_mode == 2:
        icon_mode = folium.Icon(icon='info-sign', color='orange')
    elif icon_mode == 3:
        icon_mode = folium.Icon(icon='camera', color='beige')
    else:
        icon_mode = None

    folium.Marker(location=coords, popup=f'<i>{coords[0]}, {coords[1]}</i>', tooltip=f'<b>{name}</b>', icon=icon_mode).add_to(m)
    m.save(r'D:\Программирование\Python начало\Jack_PersonalAssistant\Непрограммная часть\_!_Используемая_инфа\carta.html')

    homeland_coordinates = [47.0316, 28.8620]
    myLocation = [40.676762, 24.521355]  # Заглушка

if __name__ == '__main__':
    # print(get_ip_info('ip'))
    # print(get_ip_info('lat'))
    # print(get_ip_info('lon'))



    # print(get_coordinates('Shopping MallDova'))



    # start = (29.979541163236533, 31.13429845700044)
    # finish = (29.985744973230098, 31.13305021899803)
    # try:
    #     way_to(st_lat=start[0], st_lon=start[1], fin_lat=finish[0], fin_lon=finish[1])
    #     # input()
    # finally:
    #     sleep(5)
    #     browser_quit()



    # coords = [float(i) for i in input('Введите координаты места: ').split(',')]
    # name = input('Введите название места: ')
    # if name =='':                                   # нужно только для теста
    #     name = 'New Location'
    # icon = int(input('Выберете вариант иконки: '))
    # add_location(coords=coords, name=name, icon_mode=icon)

    # delete_location()
    # input()
    pass
