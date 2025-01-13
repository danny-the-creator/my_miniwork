import wikipedia as wiki
from colorama import Fore
import re
def wikisearch(query, lang = 'ru', voice = 'off'):
    wiki.set_lang(lang)
    try:
        page = wiki.page(query)
    except wiki.DisambiguationError:
        if voice != 'off':
            # speak(f'{Fore.LIGHTRED_EX}Ваш запрос должен быть конкретнее!{Fore.RESET}' if lang == 'ru' else f'{Fore.LIGHTRED_EX}Your request should be more accurate!{Fore.RESET}')
            pass
        return f'{Fore.LIGHTRED_EX}Ваш запрос должен быть конкретнее!{Fore.RESET}' if lang == 'ru' else f'{Fore.LIGHTRED_EX}Your request should be more accurate!{Fore.RESET}'
    except wiki.PageError:
        if voice != 'off':
            # speak(f'Мне не удалось ничего найти по вашему запросу...' if lang == 'ru' else f'I haven\'t found anything on this query...')
            pass
        return f'Мне не удалось ничего найти по вашему запросу...' if lang == 'ru' else f'I haven\'t found anything on this query...'
    def summary_split():                                                                # Можно использовать не только здесь
        text = page.summary.replace('\n', '')
        begin = 0
        result = ''
        while True:
            end = re.search(' ', str(text[begin + 150:]))
            if end == None:
                result += text[begin:]
                break
            paragraph = text[begin:begin+150] + text[begin+150 : begin+150+end.span()[0]]
            result += paragraph+'\n'
            begin = begin+150+end.span()[0] + 1
        return result
    link = page.url
    title = page.title
    summary = summary_split()

    short_end = re.search('\.|;|!', str(summary[200:]))
    short_info = re.sub(r'\(.{3,}\)', '', summary[:200] + summary[200:200 + short_end.span()[0]], count=1)

    beginning = 'Тема Запроса:  ' if lang == 'ru' else 'Request Topic:  '
    ending = 'Ссылка на полную статью:  ' if lang == 'ru' else 'For more information:  '
    if voice != 'off':
        # speak(f'{beginning}  {title}. {short_info}. ')
        print('Функция пока недоступна...')
    return f'{beginning}{Fore.LIGHTGREEN_EX}< {title.upper()} >{Fore.RESET}\n\n' \
           f'{summary}\n' \
           f'{ending}{link}'

if __name__ == '__main__':
    text = input('Введите запрос: ')
    lang = input('Введите язык запроса [en/ru/fr/de...]: ')
    print(wikisearch(text, lang=lang))


# print(result.url)
# print(Fore.LIGHTGREEN_EX + result.title.upper() + Fore.RESET)
# print(result.summary)
# print(wiki.summary('Python', sentences = 1))


# print(result.content)                                     # Не нужен!
# print(result.html())                                      # Не нужен!
# print(result.original_title)                              # Хз в чём отличие
# print(result.pageid)                                      # Не нужен!
# print(result.references)                                  # Скорее всего не нужно
# print(result.sections)                                    # Хз что это...
