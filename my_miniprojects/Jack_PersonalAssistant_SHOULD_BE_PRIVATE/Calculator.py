from colorama import Fore
import re
def space_deleter(text):
    """Cоздаёт список из введённого предложения, разбивая его по пробелам, но игнорируя множественные пробелы"""
    split = text.split(' ')
    return " ".join([i for i in split if len(i) != 0])
def calculate(task, voice = 'on'):
    comment = ''
    if voice == 'on':
        # Преобразование сказанного, в текст понятный для вычислений
        input_task = task
        task = task.replace(' млн', '000000')
        task = task.replace(' млрд', '000000000')

        task = task.replace('один', '1')
        task = re.sub(r' (триллион)|(триллиона)|(триллионов)', '000000000000', task)
        split_numbers = re.findall(r'-[\d{1,} ]{1,}|[\d{1,} ]{1,}', task)                  # находит все номера, которые воспринялись отдельно как (15000000 1)   # нужна замена
        for split_number in split_numbers:
            if space_deleter(split_number) != '':
                task = task.replace(split_number, str(eval(space_deleter(split_number).replace(' ', '+'))))
        task = task.replace(',', '.')
        task = task.replace('минус', '-')
        task = task.replace('x', '*').replace('умноженное на', '*')
        task = task.replace('подели на ', '/').replace('поделить на ', '/').replace('деленное на ', '/').replace('делённое на ', '/')
        if bool(re.search(r'на', task)) == True:
            task = task.replace('на', '*')
            comment = 'Ваше "на" было воспринято как "*", впредь говорите НОРМАЛЬНО!'

        task = task.replace(' из', '')              # облегчает извлечение корня
        root_list = re.findall(r'корень\d+', task)            # {1,} заменён на "+" (да, так можно)
        for root in root_list:
            task = task.replace(root, root.replace('корень', '')+'**0.5')
        task = task.replace('в квадрате', '**2').replace('в кубе','**3')
        task = task.replace('в степени ', '**')

        all_in_brackets = re.findall(r'вс[её] в скоб[^ -1234567890]{,5}|вс[её]|в скоб[^ -1234567890]{,5}', task)          # находитвсе команды 'всё в скобках'
        task = len(all_in_brackets) * '(' + re.sub(r'вс[её] в скоб[^ -1234567890]{,5}|вс[её]|в скоб[^ -1234567890]{,5}', ')' , task)
                    # Заменяет все команды на ')' и добавляет столько скобок в начале, сколько команд было введено (! может не работать, скорее всего работает)

        task = re.sub('скоб[^ -1234567890]{,5} закры[^ -1234567890]{,8}|закры[^ -1234567890]{,8}' , ')', task)     # [^ -1234567890] - любой символ, кроме пробела,
        task = re.sub('скоб[^ -1234567890]{,5} откры[^ -1234567890]{,8}|скоб[^ -1234567890]{,5} ', '(', task)                               # минуса и любой цифры

    # Сами вычисления
    try:
        result = f'Ответ: {Fore.LIGHTGREEN_EX}{eval(task)}{Fore.RESET}'
        result+=f'\n\nВведённый пример: {input_task}\nРаспознано как: {task}'           #! Вариант для тестирования
    except ZeroDivisionError:
        result = 'Ты серьёзно решил поделить на 0?'
    except:
        result = 'Пример введён некорректно!'
        if voice == 'on':
            result+=f'\nВведённый пример: {input_task}'
    return result

if __name__ == '__main__':
    task = input('Введите пример: ')
    print(calculate(task=task,voice='on'))

    # print(calculate(task=task, voice='off'))



# (15456321 * (5/2) ** 2) * -10 = -966020062.5
# Команда звучала так: 15 млн 456320 1 x скобка открывается 5 / 2 скобка закрывается в квадрате всё в скобках умноженное на - 10


# data = input('Введите пример: ')
# result = eval(data)
# print(result)