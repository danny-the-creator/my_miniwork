# !!! Работа со строками не используя сторонние библиотеки (без решки)
text = 'Hello world!'
print('world' in text)                          # Python может проверять наличие одной строки в другой и без модуля 're'
print(text.find('world'))                       # Выводит порядковый номер начала строки, которую мы ищем (без модуля 're') вернёт -1, если строка не входит
                                                                        # ! также find можно сократить поиск (к примеру чтобы он начинался с 5 элемента и заканчивался 20)
# print(text.index('aboba'))                      # Делает тоже самое, что и find, но если не находит, выводит ошибку

print(text.startswith(('Hello', 'Hi', 'Nice to see you')))          # !!! Проверяет, начинается ли строка со слов в картедже, если да, выводит True (БЕЗ МЕТОДА 're'!!!)
print(text.endswith((('Hello', 'Hi', 'Nice to see you'))))          # Аналог функции выше, но проверяет с конца
print(text.count('l'))                                              # Выводит количество строк в большей строке (! Тоже можно ограничить поиск)

text = '           4   3            5                 3           6             5 7 8'
print(text.split())                                             # Если метод сплит вызвать без аргумента (None), то метод разделит строку по проблеам (а пустые элементы списка
                                                                                                                        # УДАЛИТ!!! (space_deleter - БЕСПОЛЕЗЕН :( )
text.strip('_71*')                                              # strip может принимать в аргумент символы, которые он буде удалять слева и справа ото вашей строки

# Многие из методов имеют аналоги, которые выполняют тоже самое но начинают с КОНЦА строки (чаще всего не нужно)

# ФОРМАТИРОВАНИЕ - подставление частной информации в общий шаблон
# реализуется с помощью метода format
text = '{capital} is a capital of {country}'
print(text.format(capital= 'London', country = 'Great Britain'))            # format - можно использовать и с именованными аргументами


# First Program
text = input()
replaced, replacement = input(), input()
result = 0
while replaced in text:
    if result > 1000:
        result = 'Impossible'
        break
    text = text.replace(replaced,  replacement)
    result += 1
print(result)

# Final Program
text = input()
search = input()
result = 0
for i in range(len(text)):
    if text.startswith(search):
        result += 1
    text = text[1:]
print(result)
