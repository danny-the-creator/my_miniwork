from gtts import gTTS
import pyglet
import os
from time import sleep
def speak(text, language = "ru"):
    # pg.mixer.music.set_volume(0.02)
    PATH = r'D:\Программирование\Python начало\Jack_PersonalAssistant\Непрограммная часть\Не_трогать(костыль)\{}'
    filename = 'file_3s6ef9ivg0hjnhjm.mp3'
    tts = gTTS(text=text, lang=language)
    tts.save(PATH.format(filename))
    music = pyglet.media.load(PATH.format(filename), streaming=False)
    music.play()
    sleep(music.duration)
    try:
        os.remove(PATH.format(filename))
    except FileNotFoundError:
        pass
    # pg.mixer.music.set_volume(volume)
if __name__ == '__main__':
    speak("Привет этот чудестный мир!")
    speak("Hello this damn World! Another good day to die!", 'en')
    speak("Here you can find the general entry requirements to Saxion", 'en')
    speak('Потом решила выбрать более общее название, ведь от наличия GUI суть не меняется. На всякий случай поясню, консоль в данном случае — терминал Linux или знакомая пользователям Windows командная строка.', language='ru')
