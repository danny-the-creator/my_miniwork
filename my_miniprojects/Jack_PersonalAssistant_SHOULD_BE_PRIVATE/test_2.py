import folium
from colorama import Fore
import pickle

# GLOBAL
homeland_coordinates = [47.0316, 28.8620]
myLocation = [40.676762, 24.521355]                          # Заглушка
WorldMap = None

# HomeLand_icon = folium.features.CustomIcon(r'D:\Программирование\Python начало\Jack_PersonalAssistant\Непрограммная часть\Звуки_и_фото\Home.png', icon_size=(66,55))

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

while True:
    # coords = [float(i) for i in input('Введите координаты места: ').split(',')]
    # name = input('Введите название места: ')
    # if name =='':                                   # нужно только для теста
    #     name = 'New Location'
    # icon = int(input('Выберете вариант иконки: '))
    # add_location(coords=coords, name=name, icon_mode=icon)
    # delete_location()
    # input()