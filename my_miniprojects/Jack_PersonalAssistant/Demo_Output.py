import pyttsx3
tts = pyttsx3.init(driverName='sapi5')
voices = tts.getProperty('voices')
tts.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0')
# tts.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
# tts.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
text = input("Введите какой-то текст: ")
tts.say(text)                   # сначала пк скажет это (1)
print("Мой голос ужасен!")      # но первым будет выведен этот текст (0)
tts.say("Мой голос ужасен!")    # потом он скажет это (2)
tts.runAndWait()                # на данном моменте запускается озвучка текста
print("Текст после голосовой озвучки")