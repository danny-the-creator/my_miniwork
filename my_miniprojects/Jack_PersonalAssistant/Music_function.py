import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '0'         # Нужно, чтобы избавится от приветствия pygame
import pygame as pg

import random
from colorama import Fore
import re
from time import sleep
import pickle
import threading as thr                                 # Is needed for multithreading (многопоточность)
# GLOBALS
PATH = r'C:\Users\danny\Music\{}'
volume = 0.5
new_tracks_number = 12

pause_control = 42
REPEAT = -1
current_playlist = ''
current_music = ''

def like_list():
    with open(r'D:\Программирование\Python начало\Jack_PersonalAssistant\Непрограммная часть\Не_трогать(костыль)\Like.pickle', 'rb') as f:
        return pickle.load(f)
def black_list():
    with open(r'D:\Программирование\Python начало\Jack_PersonalAssistant\Непрограммная часть\Не_трогать(костыль)\Black_List.pickle', 'rb') as f:
        return pickle.load(f)
def the_newest(n):
    '''Возвращает n самых новых песен'''
    dict_of_file = {os.path.getmtime(PATH.format(i)) : i for i in os.listdir(PATH.format('')) if bool(re.search(r'\.mp3', i)) == True}
    dict_of_file_sorted = {i[1] : i[0] for i in sorted(dict_of_file.items())[::-1]}
    return list(dict_of_file_sorted.keys())[:n]

PLAYLISTS = {
    'Awa_Max' :  {'Alan_Walker,_Ava_Max_-_Alone,_Pt_II.mp3', 'Ava_Max_-_Salt.mp3', 'Ava_Max_-_So_Am_I.mp3', 'Ava_Max_-_Take_You_To_Hell.mp3', "Ava_Max_-_Who's_Laughing_Now.mp3"},
    'Alan_Walker' : {'Alan_Walker,_AuRa,_Tomine_-_Dark_Side_(YT_ver).mp3', 'Alan_Walker,_Ava_Max_-_Alone,_Pt_II.mp3', 'Alan_Walker,_K-391,_Emeli_-_Lily.mp3', 'Alan_Walker,_Sabrina_Carp_-_On_My_Way.mp3'},
    'Avenged_Sevenfold' : {'avenged-sevenfold_-_so-far-away.mp3', 'Avenged_Sevenfold-Blinded_in_Chains.mp3', 'Avenged_Sevenfold-Hail_to_the_King.mp3', 'Avenged_Sevenfold_-_Acid_Rain.mp3', 'Avenged_Sevenfold_-_Afterlife.mp3', 'Avenged_Sevenfold_-_Buried_Alive.mp3', 'Avenged_Sevenfold_-_Nightmare.mp3', 'Avenged_Sevenfold_-_Unholy_Confessions.mp3'},
    'Nightcore' : {'ERKnightcore_-_Your_Love_Is_My_Drug_(KE$.mp3', 'Msrayray6532_-_All_the_things_she_said_(.mp3', 'Nightcore_-_911_+.mp3', 'Nightcore_-_How_Do_You_Do.mp3', 'Nightcore__-_Animal_(Lyrics).mp3', 'Ram__nightcore_remix_-_Rockefeller_Street_.mp3', 'Syrex_-_Nightcore_-_WONDERLAND_-_.mp3', 'U_N_D_E_R_D_O_G_S_-_Nightcore_911_[lyrics].mp3'},
    'СерьГа' : {'СерьГа_-_Мой_друг.mp3', 'СерьГа_-_Солнечный_Чародей.mp3', 'СерьГа_-_Чертёнок_(Ты_мало_запроси.mp3', 'СерьГа_-_Я_-_Бурый_Медведь.mp3', 'СерьГа_-_Я_люблю_поезда.mp3'},
    'Anime' : {'1_опенинг_2_сезон_(Shinzo_-_Атака_Титанов_(Attack_on_.mp3','Rika_Mayama_-_Liar_Mask_(2_ОП_Убийца_Ак.mp3', 'Владыка_-_Владыка_3_.mp3', '_Nightmare_-_Эндинг_1_аниме_Тетрадь_См.mp3', 'Overlord_-_Владыка_2.mp3', '7_смертных_грехов_-_7_смертных_грехов_Опенинг.mp3', 'attack_on_titan_op5_-_опенинг_5_сезон_3_атака_т.mp3', 'Evangelion_-_Опенинг_.mp3', 'Goblin_Slayer_-_Убийца_Гоблинов_OP.mp3', 'Minami_-_[OP]_Kawaki_Wo_Ameku.mp3', 'Opening_-_One-punch_Man.mp3', 'Shinsei_Kamattechan_-_Атака_Титанов_4_сезон_OP.mp3', '[Mirai_Nikki_OP]_Yousei_T_-_OP_1.mp3', 'Врата;Штейна_-_Opening.mp3', 'Клинок,_рассекающий_Демон_-_Ending_Full.mp3', 'коносуба__-_Опенинг_1.mp3', 'опенинг_-_КЛИНОК_РАССЕКАЮЩИЙ_ДЕМОНО.mp3', 'Опенинг_2_-_Коносуба_.mp3', 'Тетрадь_Смерти_-_Ending-2_Full_HQ.mp3', 'Семь_смертных_грехов._-_3.mp3' ,'Anime_-_Военная_хроника_маленькой.mp3'},
    'Russian_music' : {'Boney_M._-_Rasputin.mp3', 'Robbie_Williams_-_Party_Like_a_Russian.mp3',  'Король_и_Шут_-_Дурак_и_молния.mp3', 'Ж.Рождественская_-_Гадалка_(из_к-ф_Ах,_водев.mp3', 'Сергей_Лазарев_-_Новый_год.mp3', 'Король_и_Шут_-_Кукла_Колдуна.mp3', 'SayMaxWell_-_Ведьмаку_заплатите_чеканн.mp3', 'Муслим_Магомаев_-_Королева_красоты_.mp3', 'Агата_Кристи_-_Как_на_войне.mp3', 'Звери_-_Районы-кварталы.mp3', 'Кватро_-_А_снег_идёт.mp3', 'Андрей_Губин_-_Ночь.mp3'},
    'Without_words' : {'DJ_Bagaikan_-_Langit_Di_Sore_Hari_(tik-.mp3', 'Tommee_Profitt_-_Moonlight_Sonata_Mvt_3.mp3', 'Kirby_dream_land_theme_so_-_theme_song_.mp3', 'Arvid_Häggström_-_GOSPEL.mp3', "Anime_your_Music_-_At_Doom's_Gate.mp3", 'Неизвестен_-_y2metacom_-_Rick_and_Mor.mp3'},
    'Chilling_Music' : {'The_Rare_Occasions_-_Notion.mp3', 'Electric_Light_Orchestra_-_Mr_Blue_Sky.mp3', 'Charlie_Puth_-_Betty_Boop_(Remix_by_Blan.mp3', 'Неизвестен_-_y2metacom_-_Rick_and_Mor.mp3', 'Kavinsky_-_Nightcall.mp3', 'The_Rare_Occasions_-_Notion.mp3', 'Duncan_Laurence_-_Arcade.mp3', 'ERKnightcore_-_Your_Love_Is_My_Drug_(KE$.mp3', 'Goldfinger_-_Superman.mp3', 'Avenged_Sevenfold_-_Acid_Rain.mp3', 'Enigma_-_Ameno_Dorime_(remix).mp3', 'Maroon_5_-_Payphone.mp3', 'Fleur_Douces_-_Homeless_Soul.mp3', 'Ali_--_Wild_Side_-_English_cover.mp3', 'TRAP_►_BoyPanda_&_VinDon_-_Deja_Vu_(Magic_Release).mp3', 'Avicii_-_The_Nights.mp3', '_Nightmare_-_Эндинг_1_аниме_Тетрадь_См.mp3', 'Sub_Urban_-_Cradles.mp3', 'twocolors_-_Lovefool.mp3', 'A_Touch_Of_Class_-_Thinking_Of_You.mp3', 'Rixton_-_Me_And_My_Broken_Heart.mp3', 'NIVIRO_-_The_Labyrinth_[NCS_Releas.mp3', 'Gym_Class_Heroes_feat._Ad_-_Stereo_Hearts_(feat._Adam.mp3', 'Alan_Walker,_K-391,_Emeli_-_Lily.mp3', 'Boy_With_Uke_-_Toxic_(Lyrics).mp3', '279empirebeats_-_Shinitai-chan.mp3', 'Alan_Walker,_AuRa,_Tomine_-_Dark_Side_(YT_ver).mp3', 'Coolio_feat_LV_-_Gangsta\'s_Paradise_(feat.mp3', 'Tommee_Profitt_-_Moonlight_Sonata_Mvt_3.mp3' },
    'Game_Memories_Colection' : {'Goldfinger_-_Superman.mp3', 'Ali_--_Wild_Side_-_English_cover.mp3', 'Black_Gryph0n_&_Baasik_-_INSANE_(A_Hazbin_Hotel_So.mp3', 'The_Living_Tombstone_-_My_Ordinary_Life.mp3', 'SayMaxWell_-_Ведьмаку_заплатите_чеканн.mp3', 'Initial_D_-_Deja_Vu.mp3', 'TRAP_►_BoyPanda_&_VinDon_-_Deja_Vu_(Magic_Release).mp3', 'Portal_2_-_This_Is_Aperture.mp3', 'DAGames_-_Build_Our_Machine.mp3', "Anime_your_Music_-_At_Doom's_Gate.mp3", 'Звери_-_Районы-кварталы.mp3', 'Gym_Class_Heroes_feat._Ad_-_Stereo_Hearts_(feat._Adam.mp3', "HAZBIN_HOTEL_-_Alastor's_Game_[ROCK_Song.mp3" },
    'Ispano_Italiano' : {'Indila_-_Ainsi_bas_la_vida.mp3', 'Indila_-_dernière_dance(remix).mp3', 'Enigma_-_Ameno_Dorime_(remix).mp3', 'Era_-_Dorime_Ameno.mp3', 'Arvid_Häggström_-_GOSPEL.mp3', 'TRAP_►_BoyPanda_&_VinDon_-_Deja_Vu_(Magic_Release).mp3' },
    'Hard_music' : {"HAZBIN_HOTEL_-_Alastor's_Game_[ROCK_Song.mp3", 'Syrex_-_Nightcore_-_WONDERLAND_-_.mp3', 'Jagwar_Twin_-_Happy_Face.mp3', 'Nathan_Evans_-_Wellerman.mp3', 'Discord_The_Living_Tombstone,_Eurobeat_Brony.mp3', 'Anime_your_Music_-_At_Doom\'s_Gate.mp3', 'Aronchupa_-_I\'m_an_Albatroz_(original.mp3', 'Linkin_Park_-_Bleed_It_Out.mp3', 'Finger_Eleven_-_Paralyzer.mp3', 'Disco_Brothers_-_Boogie_Wonderland.mp3', 'Arvid_Häggström_-_GOSPEL.mp3', 'Måneskin_-_I_WANNA_BE_YOUR_SLAVE.mp3', 'Basstrologe_-_Somebody_To_Love.mp3', 'Måneskin_-_Beggin\'.mp3', 'Avenged_Sevenfold_-_Nightmare.mp3', 'Halsey_-_Walls_Could_Talk.mp3', 'Boney_M._-_Rasputin.mp3', 'DragonForce_-_Through_The_Fire_And_Flam.mp3', 'Green_Day_-_Holiday.mp3', 'Nightcore_-_How_Do_You_Do.mp3', 'Владыка_-_Владыка_3_.mp3', 'Maroon_5_-_Wake_Up_Call.mp3', 'Michael_Jackson_-_In_the_Closet.mp3', 'Imagine_Dragons_-_Believer.mp3', 'Robbie_Williams_-_Party_Like_a_Russian.mp3', 'ACRAZE_feat_Cherish_-_Do_It_To_It.mp3', 'Powerwolf_-_In_the_Name_of_God_(Deus_.mp3', 'Avenged_Sevenfold_-_Unholy_Confessions.mp3' },
    'Funny_music' : {'The_Irish_Rovers_-_Drunken_Sailor.mp3', 'Coolio_feat_LV_-_Gangsta\'s_Paradise_(feat.mp3', 'Ram__nightcore_remix_-_Rockefeller_Street_.mp3', 'Halsey_-_Walls_Could_Talk.mp3', 'Green_Day_-_Holiday.mp3', 'Msrayray6532_-_All_the_things_she_said_(.mp3', 'Maroon_5_-_Payphone.mp3', "Måneskin_-_Beggin'.mp3", 'Alan_Walker,_Sabrina_Carp_-_On_My_Way.mp3', 'Bella_Poarch_-_Build_a_Bitch.mp3', 'THE_BEATLES_-_Eleanor_Rigby.mp3', 'Britney_Spears_-_Toxic.mp3', 'Discord_The_Living_Tombstone,_Eurobeat_Brony.mp3', 'Bebe_Rexha_-_Self_Control.mp3', 'Meghan_Trainor_-_Title.mp3', 'Sia_-_The_Greatest.mp3', 'Little_Big_-_UNO.mp3', 'Imagine_Dragons_-_Thunder.mp3', 'Anastacia_-_Defeated.mp3', "Shania_Twain_-_That_Don't_Impress_Me_Muc.mp3", 'David_Guetta,_Bebe_Rexha,_-_Say_My_Name.mp3', "Kesha_-_Don't_stop.mp3", 'Alexander_Rybak_-_Fairytale.mp3', 'Natalie_Summer_-_Kings_And_Queens.mp3', 'Alan_Walker,_Ava_Max_-_Alone,_Pt_II.mp3', 'Ava_Max_-_Salt.mp3', 'Ava_Max_-_So_Am_I.mp3', 'Ava_Max_-_Take_You_To_Hell.mp3', "Ava_Max_-_Who's_Laughing_Now.mp3"},

    'Like' : like_list(),
    'Black_List' : black_list(),
    'New' : the_newest(new_tracks_number)
}

def space_deleter(text):
    """Cоздаёт список из введённого предложения, разбивая его по пробелам, но игнорируя множественные пробелы"""
    split = text.split(' ')
    return " ".join([i for i in split if len(i) != 0])
def history():
    global music_history, current_music
    if len(music_history) == 0:  # Решает проблему при первом запуске
        music_history.append(current_music)
    if current_music.replace('!', '') != music_history[-1].replace('!', ''):              # Eсли музыка была запущена второй раз подряд, она не будет добавлена в историю
        while current_music in set(music_history):                      # Восклицательные знаки убираются, так как нам важно содержание файла, а не еги имя в истории
            current_music = current_music + '!'
        music_history.append(current_music)
def random_music():
    global current_playlist,current_music, PLAYLISTS
    if current_playlist == '':
        current_music = PATH.format(random.choice(music_names))
    else:
        if PLAYLISTS[current_playlist] == set():
            print('К сожалению этот плейлист пуст, но вы можете это исправить!\n')
            pg.mixer.music.stop()
            current_playlist = ''
            return 'stop'
        else:
            current_music = PATH.format(random.choice(list(PLAYLISTS[current_playlist])))
    pg.mixer.music.load(current_music)
    pg.mixer.music.play(REPEAT)

def next():
    global current_music, next_track, pause_control, current_playlist, music_history
    if next_track == []:
        random_music_result = random_music()  # Функция автоматически выполняется, а её результат в случае 'stop' записывается в 'result'
        if random_music_result != 'stop':
            pause_control = abs(pause_control)
            history()
    else:
        if current_playlist != '' and next_track[0] not in PLAYLISTS[current_playlist]:
            current_playlist = ''
            music_history = [current_music]
        current_music = PATH.format(next_track[0])  # Проигрывает следующий трек в списке
        next_track.remove(next_track[0])            # Удаляет трек из списка 'next_track'
        pg.mixer.music.load(current_music)
        pg.mixer.music.play(REPEAT)
        pause_control = abs(pause_control)
        history()
def autonext():
    while REPEAT != -1:
        if pg.mixer.music.get_busy() == False and pause_control > 0 and current_music != '' :
            next()
        sleep(0.42)

def minus():
    global volume
    if volume > 0.200005:
        volume -= 0.1
        pg.mixer.music.set_volume(volume)
        print('Текущая громкость = ' + str(round(volume * 10) * 10) + '%')
    elif 0.200005 > volume > 0.050005:
        volume -= 0.05
        pg.mixer.music.set_volume(volume)
        print('Текущая громкость = ' + str(int(round(volume * 10, 1) * 10)) + '%')
    elif 0.050005 > volume > 0.000005:
        volume -= 0.025
        pg.mixer.music.set_volume(volume)
        print('Текущая громкость = ' + str(int(volume * 100)) + '%')
    else:
        print('Это минимальная громкость!')
def plus():
    global volume
    if 0.150005 < volume < 0.999999:
        volume += 0.1
        pg.mixer.music.set_volume(volume)
        print('Текущая громкость = ' + str(round(volume * 10) * 10) + '%')
    elif 0.025005 < volume < 0.150005:
        volume += 0.05
        pg.mixer.music.set_volume(volume)
        print('Текущая громкость = ' + str(
            int(round(volume * 10, 1) * 10)) + '%')                  # выводит громкость в '%' (round и int нужны для округления)
    elif volume < 0.025005:
        volume += 0.025
        pg.mixer.music.set_volume(volume)
        print('Текущая громкость = ' + str(int(volume * 100)) + '%')
    else:
        print('Это максимальная громкость!')
def back():
    global music_history, current_music
    if len(music_history) == 0:
        print("Ты дурак?")
    elif len(music_history) == 1:
        print('Это последняя песня в истории просмотров')
        pg.mixer.music.play(REPEAT)
    else:
        music_history.pop()
        current_music = music_history[-1]
        pg.mixer.music.load(current_music.replace('!', ''))
        pg.mixer.music.play(REPEAT)
        print('Включаю предыдущий трек')
def like():
    global PLAYLISTS
    if current_music == '':
        print('Понял, вам нравится тишина!')
    else:
        now_is_playing = current_music.split(PATH.format(''))[1].replace('!', '')
        if now_is_playing in PLAYLISTS['Black_List']:
            PLAYLISTS['Black_List'].discard(now_is_playing)
            with open(r'D:\Программирование\Python начало\Jack_PersonalAssistant\Непрограммная часть\Не_трогать(костыль)\Black_List.pickle', 'wb') as f:
                pickle.dump(PLAYLISTS['Black_List'], f)
            print('Что ж, дадим этой песне ещё один шанс...')
        else:
            PLAYLISTS['Like'].add(now_is_playing)
            with open(r'D:\Программирование\Python начало\Jack_PersonalAssistant\Непрограммная часть\Не_трогать(костыль)\Like.pickle', 'wb') as f:
                pickle.dump(PLAYLISTS['Like'], f)
            print('Мне она тоже понравилась!')
def dislike():
    global PLAYLISTS
    if current_music == '':
        print('А кому нравится молчание?')
    else:
        now_is_playing = current_music.split(PATH.format(''))[1].replace('!', '')
        if now_is_playing in PLAYLISTS['Like']:
            PLAYLISTS['Like'].discard(now_is_playing)
            with open(r'D:\Программирование\Python начало\Jack_PersonalAssistant\Непрограммная часть\Не_трогать(костыль)\Like.pickle', 'wb') as f:
                pickle.dump(PLAYLISTS['Like'], f)
            print('Что ж, вкусы меняются...')
        else:
            PLAYLISTS['Black_List'].add(now_is_playing)
            with open(r'D:\Программирование\Python начало\Jack_PersonalAssistant\Непрограммная часть\Не_трогать(костыль)\Black_List.pickle', 'wb') as f:
                pickle.dump(PLAYLISTS['Black_List'], f)
            print('Добавил в чёрный список')

music_history = []
next_track = []

pg.mixer.init()
pg.mixer.music.set_volume(volume)

while True:
    music_names = list({i for i in os.listdir(PATH.format('')) if bool(re.search(r'\.mp3', i)) == True} - PLAYLISTS['Black_List']) + list(PLAYLISTS['Like'])
    text = input("Введите вашу команду: ")
    command = space_deleter(text)
    if command == '=' or command == '':
        if pause_control > 0:
            pg.mixer.music.pause()
            print('Музыка на паузе')
        elif pause_control < 0:
            pg.mixer.music.unpause()
            print('Продолжаю')
        pause_control *= -1
    elif command == '-':
        minus()
    elif command == '+':
        plus()
    elif command in {'random', 'rand', 'r', '%'}:
        random_music_result = random_music()                # Функция автоматически выполняется, а её результат в случае 'stop' записывается в 'result'
        if random_music_result != 'stop':
            pause_control = abs(pause_control)
            history()
            print('Ура, мой выбор!')
    elif command == '>':
        next()
        print('Понял, следующая!')
    elif command == '<':
        pause_control = abs(pause_control)
        back()
    elif command == 'play' or command == 'repeat' or command == 'повтори':
        pg.mixer.music.play(REPEAT)
        pause_control = abs(pause_control)
        print('Включаю музыку')
    elif command.split(' ')[0].lower() in {'включи', 'play', 'p-', '-p'}:
        if command.split(' ')[1] in PLAYLISTS['Black_List']:
            print('Данная песня в чёрном списке, вы действительно хотите послушать её?')
            while True:
                choice = input('Да или Нет?\n')
                if choice.lower() in {'да', 'yes', '+', 'ага'}:
                    print('Окей, я просто предупредил...')
                    choice = 'yes'                                              # Это тоже вроде не нужно если поместить всё в функцию
                    break
                elif choice.lower() in {'no', 'not', '-', 'нет', 'не'}:
                    print('Как и ожидалось')                                    # В функцию можно просто: return 'Как и ожидалось'
                    choice = 'no'                                                       # Тогда это не нужно
                    break                                                               # Это тоже
            if choice == 'no':                                                          # И это
                print()                                                                 # И это
                continue                                                                # И это
        if current_playlist != '' and command.split(' ')[1] not in PLAYLISTS[current_playlist]:
            current_playlist = ''
            music_history = [current_music]
        current_music = PATH.format(command.split(' ')[1])
        try:
            pg.mixer.music.load(current_music)
        except pg.error:
            print('Мне не удалось найти этот трек...')
            print('Возможно вы неправильно ввели название, или данный трек просто ещё не скачен \n')
            continue                                                                    # надо будет заменить на return
        pause_control = abs(pause_control)
        pg.mixer.music.play(REPEAT)
        history()
        print('Как вам будет угодно')
    elif command.split(' ')[0].lower() in {'playlist:', 'playlist', ':'} or command in {'^', ':-', ':#', 'quitp'}:
        next_track = []                                             # При использовании плейлистов каждый следующий трек будет выходить из плейлиста
        if command.lower() in {'playlist:', 'playlist', ':'}:
            print('Какой плейлист? Я тип угадать должен?\n')
            sleep(2)
            print('... ... ...\n')
            sleep(1.75)
            print('Ладно...')
            sleep(1.25)
            current_playlist = random.choice([str(i) for i in PLAYLISTS.keys() if PLAYLISTS[i] != set()])
            print(f'Мой выбор: {Fore.LIGHTBLUE_EX}{current_playlist}{Fore.RESET}')
            current_music = PATH.format(random.choice(list(PLAYLISTS[current_playlist])))
            pg.mixer.music.load(current_music)
            pg.mixer.music.play(REPEAT)
            pause_control = abs(pause_control)
            music_history = [current_music]
        elif command in {'^', ':-', ':#', 'quitp'} or command.split(' ', 1)[1] in {'-', 'end', '#', 'back', 'quitp', 'выйти', }:
            if current_playlist == '':
                print('Это тебе не плейлист чтобы из него выходить!')
            else:
                current_playlist = ''
                music_history = [current_music]
                pg.mixer.music.stop()
                pause_control = -abs(pause_control)
                print('Выхожу из плейлиста, сэр')
        elif command.split(' ', 1)[1] in PLAYLISTS.keys():
            if command.split(' ', 1)[1] == current_playlist:
                print('Вы уже слушаете этот плейлист!')
                print('Для переключения треков используйте ">"')
            else:
                current_playlist = command.split(' ', 1)[1]
                if PLAYLISTS[current_playlist] == set():
                    print('К сожалению этот плейлист пуст, но вы можете это исправить!')
                    current_playlist = ''
                else:
                    current_music = PATH.format(random.choice(list(PLAYLISTS[current_playlist])))
                    pg.mixer.music.load(current_music)
                    pg.mixer.music.play(REPEAT)
                    pause_control = abs(pause_control)
                    music_history = [current_music]
                    print(f'Включаю плейлист {Fore.LIGHTBLUE_EX}{current_playlist}{Fore.RESET}')
        else:
            print('Такого плейлиста не существует')
    elif command.split(' ')[0].lower() in {'next', 'next:', 'nextlist', 'следующая', 'след', '->', 'n', 'n:', 'nl'}:
        if command.lower() in {'next', 'next:', 'nextlist', 'следующая', 'след', '->', 'n', 'n:', 'nl'}:
            print(f'Очередь Воспроизведения: {Fore.GREEN}{next_track}{Fore.RESET}'.replace('[]', 'Пусто'))
        elif command.split(' ')[1] not in next_track:
            if command.split(' ')[1] in music_names:
                next_track.append(command.split(' ')[1])
                print(f"Трек {Fore.GREEN}{command.split(' ')[1]}{Fore.RESET} успешно добавлен в очередь воспроизведения")
            elif command.split(' ')[1] in PLAYLISTS['Black_List']:
                print('Данная песня в чёрном списке, вы действительно хотите добавить её в очередь?')
                while True:
                    choice = input('Да или Нет?\n')
                    if choice.lower() in {'да', 'yes', '+', 'ага'}:
                        print('Окей, я просто предупредил...')
                        choice = 'yes'                                            # Это тоже вроде не нужно если поместить всё в функцию
                        break
                    elif choice.lower() in {'no', 'not', '-', 'нет', 'не'}:
                        print('Как и ожидалось')                                  # В функцию можно просто: return 'Как и ожидалось'
                        choice = 'no'                                             # Тогда это не нужно
                        break                                                     # Это тоже
                if choice == 'no':                                                # И это
                    print()                                                       # И это
                    continue                                                      # И это
                next_track.append(command.split(' ')[1])
                print(f"Трек {Fore.GREEN}{command.split(' ')[1]}{Fore.RESET} успешно добавлен в очередь воспроизведения")
            else:
                print('Я не могу поставить в очередь трек, которого нет!')
        else:
            print('Данный трек уже присутствует в очереди, ожидайте')
    elif command == 'название' or command == 'имя' or command == 'name' or command == '?':
        if current_music != '':
            now_is_playing = current_music.split(PATH.format(''))[1].replace('!', '')
            print(f'Сейчас играет: {Fore.LIGHTBLUE_EX}{current_playlist}{Fore.RESET} {Fore.GREEN}{now_is_playing}{Fore.RESET}')  # 'LIGHTBLUE_EX' или 'RED'
        else:
            print(f'Сейчас вы наслаждаетесь {Fore.GREEN}Тишиной{Fore.RESET} из плейлиста {Fore.LIGHTBLUE_EX}Молчание{Fore.RESET}')
    elif command.lower() == 'playlists':
        print([i for i in PLAYLISTS.keys()])
    elif command.split(' ')[0].lower() in  {'list', 'music', 'from', 'in', 'список', '?'} and command.lower() not in {'list', 'music', 'from', 'in', 'список', '?'}:
        if command.split(' ')[1] in PLAYLISTS.keys():
            print(f'{Fore.LIGHTBLUE_EX}{command.split(" ")[1]}{Fore.RESET}: {PLAYLISTS[command.split(" ")[1]]}'.replace('set()', 'Empty'))
        else:
            print('Такого плейлиста пока что не существует')
    elif command == '!' or command.lower() == 'like':
        like()
    elif command == '/' or command == '#' or command.lower() == 'dislike':
        dislike()
    elif command.lower() in {'<>', 'повтор', '< >', '!<>', '><'}:
        REPEAT *= -1
        if REPEAT < 0:
            print('Поставил музыку на повтор')
        elif REPEAT > 0:
            print('Отключаю повтор')
            music_parallel = thr.Thread(target=autonext)
            music_parallel.start()
        try:
            pg.mixer.music.play(REPEAT)
        except pg.error:
            pass
        pause_control = abs(pause_control)
    elif command == 'exit' or command == 'stop' or command == 'end':
        print('Завершаю программу')
        volume = 0.5
        pause_control = 42
        REPEAT = -1
        current_playlist = ''
        current_music = ''
        music_history = []
        next_track = []
        break
    else:
        print("Такой команды нет!")
    print()



# if __name__ == '__main__':
#     while True:
#         text = input("Введите вашу команду: ")
#         music(text)
#         print()


# НЕ ОТНОСИТСЯ К САМОЙ ПРОГРАММЕ !!!

# #Заменяет все пробелы на "_" в указанной папке
# import os
# PATH = r'C:\Users\danny\Downloads\{}'
# list = os.listdir(PATH.format(''))
# for file in list:
#     renamed_file = file.replace(' ', '_')
#     os.rename(PATH.format(file), PATH.format(renamed_file))