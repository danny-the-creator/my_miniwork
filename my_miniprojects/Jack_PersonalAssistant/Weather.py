import re
from colorama import Fore
import pyowm.commons.exceptions
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
from Navigation import get_ip_info

# Гиперпараметры
HOMELAND = 'Кишинев'

owm = OWM('265149b85a7e21285e992960b1a681c8')
mgr = owm.weather_manager()
geo_mgr = owm.geocoding_manager()

def weather(lang = 'ru', placename = None, after = None, mod = 0):
    feels_result = precipitation_result = important = useless_info = snow_advice = rain_advice = far_future_control = vision_advice = ''
    result = f'{Fore.LIGHTRED_EX}mod = 0 | mod = 1 | mod = 2{Fore.RESET}'

    config_dict = get_default_config()
    config_dict['language'] = lang



    if placename == None:
        lat = get_ip_info('lat')
        lon = get_ip_info('lon')
        beginning = 'В вашем регионе '
    elif placename.lower() in {'home', 'base', 'shelter', 'homeland', 'дом', 'база', 'родина', 'у нас'}:
        place = geo_mgr.geocode(HOMELAND)[0]                             # Сам по себе это список, поэтому надо вывести первый (и чаще всего единственный элемент)
        coords = {'lon': place.lon, 'lat': place.lat}
        lat = coords['lat']
        lon = coords['lon']
        beginning = 'На нашей Родине '
    else:
        try:
            place = geo_mgr.geocode(placename)[0]                        # Сам по себе это список, поэтому надо вывести первый (и чаще всего единственный элемент)
            coords = {'lon': place.lon, 'lat': place.lat}
            lat = coords['lat']
            lon = coords['lon']
            beginning = f'В {placename} '                # !!! Нужно будет поиграться с названием
        except IndexError:
            return 'Я не знаю это место...'



    if after == None:
        observation = mgr.weather_at_coords(lat=lat, lon=lon)
        current_weather = observation.weather
        at_time = 'сейчас '
    else:
        if bool(re.fullmatch(r'\d{1,}-\d{1,}', after)) == False:
            return f'{Fore.LIGHTRED_EX}Нужно ввести время в формате "__-__", сначала ЧИСЛО, потом ЧАС{Fore.RESET}'

        one_call = mgr.one_call(lat=lat, lon=lon, exclude='minutely')           #  units='metric' (скорее всего это стоит по умолчанию)
        after_hour = int(after.split('-')[1])
        after_day =  int(after.split('-')[0])
        if after_day < 0 or after_hour < 0 or after_hour > 24:          # Можно заменить '>' на  '>='
            return 'Некорректно введено время'
        elif 7 >= after_day > 1:                                        # Можно заменить '>=' на  '>'
            current_weather = one_call.forecast_daily[after_day]
            far_future_control = True
            after_hour = ''
        elif after_day == 0 or after_day == 1:
            current_weather = one_call.forecast_hourly[after_day* 24 + after_hour]
        else:
            return 'Мы на такой далёки период погоду не загадываем'
        at_time = f'через {after_day} дней и {after_hour} часов будет '.replace('0 дней и ','').replace('1 дней', '1 день').replace('1 часов', '1 час')
        if far_future_control == True:                                              # В таких временых рамках часы значения не имеют
            at_time = at_time.replace('и  часов ', '')
    if far_future_control == '':
        Temperature = current_weather.temperature('celsius')['temp']        # ? colorama
        Feels_temp = current_weather.temperature('celsius')['feels_like']
    else:
        Temperature = ((current_weather.temp['day'] + current_weather.temp['eve']) / 2) - 273
        morn_result = f'    {Fore.LIGHTGREEN_EX}■{Fore.RESET} Утром - {Fore.RED}{round(current_weather.temp["morn"]-273, 1)}{Fore.RESET} °C\n'
        day_result  = f'    {Fore.LIGHTGREEN_EX}■{Fore.RESET} Днём - {Fore.RED}{round(current_weather.temp["day"]-273, 1)}{Fore.RESET} °C\n'
        eve_result  = f'    {Fore.LIGHTGREEN_EX}■{Fore.RESET} Вечером - {Fore.RED}{round(current_weather.temp["eve"]-273, 1)}{Fore.RESET} °C\n'
        feels_result = morn_result + day_result + eve_result

    Detailed_status = current_weather.detailed_status
    Humidity = current_weather.humidity
    Wind = current_weather.wnd['speed']  # wind - скорость ветра м/с    (можно поиграться) colorama
    Rain = current_weather.rain
    Snow = current_weather.snow

    Predict_rain = current_weather.precipitation_probability  # вероятность осадков

    vision = current_weather.visibility_distance  # metres
    clouds = current_weather.clouds
    heat_index = current_weather.heat_index
    weather_code = current_weather.weather_code
    dewpoint = current_weather.dewpoint  # Точка росы (Что-то на физическом)
    pressure = current_weather.pressure


    if far_future_control == '' and abs(Temperature - Feels_temp) >= 2:
        feels_result = f'Но Ощущается как {Fore.RED}{round(Feels_temp, 1)}{Fore.RESET} °C\n'

    if Snow != {}:
        duration = [i for i in Snow.keys()][-1]
        precipitation_result = f'\nЗа последние {Fore.LIGHTGREEN_EX}{duration.replace("h", "ч")}{Fore.RESET} выпало {Fore.LIGHTWHITE_EX}{Snow[duration]} мм{Fore.RESET} Снега'.replace('За последние 1ч', 'За последний час')       # Надо менять цвет!
        snow_advice ='с капюшоном'
    elif Rain != {}:
        duration = [i for i in Rain.keys()][-1]
        precipitation_result = f'\nЗа последние {Fore.LIGHTGREEN_EX}{duration.replace("h","ч")}{Fore.RESET} выпало {Fore.LIGHTCYAN_EX}{Rain[duration]} мм{Fore.RESET} Дождя'.replace('За последние 1ч', 'За последний час')         # Надо менять цвет!
        rain_advice = 'И не забудь взять Зонт!'
    else:
        if after == None:
            hours = 0
            for forecast in mgr.one_call(lat=lat, lon=lon, exclude='minutely').forecast_hourly[1:6]:
                hours += 1
                if forecast.rain != {}:
                    precipitation_result = f'\n{Fore.LIGHTGREEN_EX}Внимание{Fore.RESET}: Ожидается выпадение {Fore.LIGHTCYAN_EX}Осадков{Fore.RESET} в течении следующих {Fore.LIGHTGREEN_EX}{hours}{Fore.RESET} часов'.replace('следующих 1 часов', f'следующего {Fore.LIGHTGREEN_EX}часа{Fore.RESET}')
                    break
                else:
                    precipitation_result = '\nВ ближайшее время осадков не наблюдается'
        else:
            precipitation_result = f'\n{Fore.LIGHTCYAN_EX}Осадков{Fore.RESET} быть не должно...'


    if far_future_control == True:
        if precipitation_result != f'\n{Fore.LIGHTCYAN_EX}Осадков{Fore.RESET} быть не должно...':                      # Чтобы в случае отсутствия осадков ничего не менялось
            precipitation_result = f'\n{Fore.LIGHTGREEN_EX}Внимание{Fore.RESET}: Ожидается выпадение {Fore.LIGHTCYAN_EX}Осадков{Fore.RESET}'
        vision_result = f'{Fore.LIGHTMAGENTA_EX}Пока НЕ могу определить...{Fore.RESET}'                 # Убирает то, что нельзя определить в таком далёком будущем
        vision_advice = ''
    else:
        if vision >= 10000:
            vision_result = f'{Fore.LIGHTMAGENTA_EX}Оптимальная{Fore.RESET}, всё в полном порядке!'
        elif vision >=7000:
            vision_result = f'{Fore.LIGHTMAGENTA_EX}Ниже среднего{Fore.RESET}, где-то {Fore.YELLOW}{vision}{Fore.RESET} метров, скорее всего просто повышенная облачность'
        elif vision >= 3000:
            vision_result = f'{Fore.LIGHTMAGENTA_EX}Хреновая{Fore.RESET}, всего {Fore.YELLOW}{vision}{Fore.RESET} метров, ставлю на то что у вас сейчас туман '
            vision_advice = f'\n{Fore.LIGHTRED_EX}Плохая видимость{Fore.RESET}, аккуратнее на дорогах!'
        else:
            vision_result = f'Критично низкая, {Fore.LIGHTRED_EX}{vision}{Fore.RESET} метров, код - {Fore.LIGHTRED_EX}КРАСНЫЙ{Fore.RESET}'
            important = f'\n{Fore.LIGHTRED_EX}!!!{Fore.RESET} Видимость: ' + vision_result
            vision_advice = f'\nНа улицу лучше не выходить, {Fore.LIGHTRED_EX}ничего не видно{Fore.RESET}, потеряешься!'
    if heat_index != None and dewpoint != None:
        useless_info = f'Heat_Index: {heat_index} {Fore.LIGHTMAGENTA_EX}|{Fore.RESET} Dewpoint: {dewpoint}\n'
    elif heat_index != None:
        useless_info = f'Heat_Index: {heat_index}\n'
    elif dewpoint != None:
        useless_info = f'Точка Росы: {Fore.LIGHTBLUE_EX}{round(dewpoint-273, 1)}{Fore.RESET}°C\n'

    # ! Advice !
    advice = 'Пока что не придумал...'
    if mod == 2 and far_future_control == '':
        if Feels_temp < 0:
            temp_advice = 'На улице сейчас капец как холодно,\n'
            if snow_advice == '' and rain_advice != '':                 # Дождь или снег значения не имеют
                snow_advice = 'с капюшоном'
            if Wind >= 6:
                advice = f'{temp_advice}Одень самую тёплую куртку {snow_advice} шапку и шарф, но лучше сиди ДОМА!'
            else:
                if Detailed_status == 'ясно' and Wind <= 3.5 and snow_advice != '':
                    to_do = '\nНо можно поиграть в снегу, не забудь перчатки'
                advice = f'{temp_advice}Одень самую тёплую куртку {snow_advice} и шапку{to_do}'

        elif Feels_temp <= 12:
            temp_advice = 'На улице сейчас холодно,\n'
            if snow_advice == '' and rain_advice != '':                 # Дождь или снег значения не имеют
                snow_advice = 'с капюшоном'
            if Wind > 4 or Humidity > 50 or snow_advice != '' or Detailed_status != 'ясно':
                advice = f'{temp_advice}Одень тёплую куртку {snow_advice} и шапку'
            else:
                advice = f'{temp_advice}Но не сильно, выходить можно без шапки и без перчаток'

        elif Feels_temp > 12 and snow_advice != '':
            advice = 'Знаешь что, сиди дома, на улице СНЕГ пошёл'
        else:
            if Wind >= 4.5:
                rain_advice = 'Зонт лучше не брать, сильный ветер, поэтому найди ему замену или держи его крепче!'
            if Feels_temp < 19:
                temp_advice = 'Прохладно'
                if Detailed_status == 'ясно':
                    advice = f'{temp_advice}, но мастерки будет достаточно'
                elif Rain != {}:
                    advice = f'{temp_advice} и идёт дождь\nРекомендую дождеквик\n{rain_advice}'
                else:
                    advice = f'{temp_advice}, можешь надеть мастерку, но рекомендую ветровку'
            elif Feels_temp < 25:
                temp_advice = 'Сейчас тепло'
                if Detailed_status == 'ясно':
                    advice = f'{temp_advice}, можно выходить в футболке'
                elif Rain != {}:
                    advice = f'{temp_advice}, но... идёт дождь, надень лучше мастерку\n{rain_advice}'
                else:
                    advice = f'{temp_advice}, но советую надеть мастерку, хотя можешь и чисто в футболке выйти'
            elif Feels_temp <= 30:
                temp_advice = 'На улице довольно жарко'
                if Detailed_status == 'ясно' and Humidity <=30:
                    advice = f'{temp_advicce} и душно, если соберёшься куда-то выходить, то не забудь кепку и солнечные очки захвати'
                elif Rain != {}:
                    if Rain['1h'] >= 1.25:
                        advice = f'Сейчас дождь, лучше оставайтесь дома, если надо куда-то идти, захватите Зонт'
                    else:
                        advice = f'{temp_advice} и дождик моросит, самое время для небольшой прогулки на легке!'
                if Humidity > 60:
                    advice = f'{temp_advicce}, но вроде не душно, советую развеяться: Прогуляться и подышать свежим воздухом будет весьма кстати'
                else:
                    advice = f'{temp_advice}, без Кепки и Солнечных Очков выходить не рекомендую!'
            elif Feels_temp > 30:
                temp_advicce = 'Сегодня капец как жарко'
                if Detailed_status == 'ясно' and Humidity <=35:
                    advice = f'{temp_advicce}, если соберёшься куда-то выходить, то не забудь кепку, солнечные очки и воду, но лучше отдохни дома'
                elif Rain != {}:
                    advice = f'Сейчас дождь, советую остаться дома, если надо куда-то идти, возьми хоть кепку и Зонт'
                if Humidity > 69:
                    advice = f'{temp_advicce}, но вроде не душно, советую прогуляться, подышать свежим воздухом\nИ не забудьте Кепку'
                else:
                    advice = f'{temp_advicce}, при такой погоде, надеюсь вы сейчас отдыхаете где-то на берегу Моря...\n' \
                             f'В любом случае, Обязательно нацепите Кепку и Солнечные Очки, и не стойте долго под палящим солнцем'
            else:
                advice = 'Перекреститесь, происходит какая-то аномалия [или это мои датчики сбились...]'

    if mod == 0:
        result = f'{beginning}{at_time}{Fore.LIGHTGREEN_EX}{Detailed_status.capitalize()}{Fore.RESET}\n' \
                 f'Температура: {Fore.RED}{round(Temperature, 1)}{Fore.RESET} Градусов по Цельсию\n{feels_result}' \
                 f'Влажность: {Fore.LIGHTBLUE_EX}{Humidity} %{Fore.RESET} {Fore.LIGHTMAGENTA_EX}|{Fore.RESET} Скорость ветра: {Fore.YELLOW}{Wind} м/c{Fore.RESET} ' \
                 f'{precipitation_result}' \
                 f'{important}'
    elif mod == 1:
        result = f'Видимость: {vision_result}\n' \
                 f'Кол-во {Fore.CYAN}грозовых{Fore.RESET} облаков: {Fore.CYAN}{clouds}{Fore.RESET}\n' \
                 f'Давление: {Fore.BLUE}{pressure["press"]}{Fore.RESET} мм рт.ст. \n' \
                 f'{useless_info}' \
                 f'Код Погоды: {Fore.LIGHTGREEN_EX}{weather_code}{Fore.RESET}'
    elif mod == 2:
        result = f'{Fore.LIGHTYELLOW_EX}Совет:{Fore.RESET} {advice}{vision_advice}'
    return result
if __name__ == '__main__':
    print(weather())
    print(weather(mod=1))
    print(weather(mod=2))



# Метод 'one_call'

# one_call = mgr.one_call(lat=52.5244, lon=13.4105, exclude='minutely')           #  units='metric' (скорее всего это стоит по умолчанию)

# available exclude options are defined by the One Call API
# available values are: 'minutely', 'hourly', 'daily'
# multiple exclusions may be combined with a comma, as above