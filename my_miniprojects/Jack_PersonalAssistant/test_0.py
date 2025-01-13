import pygame
from gtts import gTTS
import pygame as pg
from tempfile import TemporaryFile
from io import BytesIO

# tts = gTTS(text='Here you can find the general entry requirements to Saxion', lang='en')
tts = gTTS(text='Потом решила выбрать более общее название, ведь от наличия GUI суть не меняется. На всякий случай поясню, консоль в данном случае — терминал Linux или знакомая пользователям Windows командная строка.', lang='ru')
fp = BytesIO()
tts.write_to_fp(fp)
fp.seek(0)
pg.mixer.init()
pg.mixer.music.load(fp)
pg.mixer.music.play()