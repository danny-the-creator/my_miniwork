from googletrans import Translator
translator = Translator()
def translate(text, intoLang=None):
    if intoLang == None:
        textLang = translator.detect(text).lang
        if textLang == 'en':
            intoLang = 'ru'
        else:
            intoLang = 'en'
    result = translator.translate(text, dest=intoLang)
    return result.text

if __name__ == '__main__':
    print(translate('Hi, it\'s me, Mario!'))



# a = translator.translate('you failed me', dest='ru')
# print(translator.detect('You are son of a beach').lang)
# print(a.text)
