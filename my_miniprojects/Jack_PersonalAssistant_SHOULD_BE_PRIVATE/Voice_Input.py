import speech_recognition
# Для дизайна ответов
from colorama import Fore
# --- --- --- --- --- --- --- ---
sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.75
PRIORITY_MIKE = {'Наушники (WH-CH510 Stereo)', 'Головной телефон (WH-CH510 Hands-Free AG Audio)', 'Головной телефон (WH-CH510 Hand'}
def listen_to_me():
    "Ваш запрос"
    if PRIORITY_MIKE & set(speech_recognition.Microphone.list_microphone_names()) == PRIORITY_MIKE:
        n = 2               # Если подключены наушники, будут использоваться они
    else:
        n = None
    try:
        with speech_recognition.Microphone(device_index = n) as mike:
            sr.adjust_for_ambient_noise(source=mike, duration=0.5)
            audio = sr.listen(source=mike)
            request = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        return request
    except speech_recognition.UnknownValueError:
        return "BULLSHIT"

def greeting():
    "Приветствует пользователя"
    return "Welcome back Commander!"
def main():
    "Как говорится: ИИ - просто набор IF и Else"
    global request
    request = listen_to_me()
    if request == "привет джек":
        print(greeting())
    elif request == "стоп":
        print("I'll see you soon!")
        quit()
    elif request == "BULLSHIT":
        print(f"I'm sorry sir, but you just said a {Fore.RED}BULLSHIT{Fore.RESET}...")
    else:
        print(f"Данная команда выходит за пределы demo-версии программы, если хотите получить доступ ко всему функционалу заплатите {Fore.LIGHTYELLOW_EX} 100 BTC {Fore.RESET}")
if __name__ == "__main__":
    # print(len(speech_recognition.Microphone.list_microphone_names()))
    while True:
        main()
        print(f"Команда звучала так: {Fore.GREEN}{request}{Fore.RESET}")
        input()