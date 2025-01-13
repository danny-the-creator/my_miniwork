from colorama import init                       #цвет фона - Back, текста - Fore
from colorama import Fore, Back, Style
init()
b = ""
print(Fore.GREEN)
example = input('Введите пример: ')
for i in example:
    if i == "*":
        c = i
        a = b
        b = ""
    elif i == "-":
        c = i
        a = b
        b = ""
    elif i == "+":
        c = i
        a = b
        b = ""
    elif i == "/":
        c = i
        a = b
        b = ""
    else:
        b = b + i
a = float(a)
b = float(b)
print(Fore.MAGENTA)
if c == '+' :
    o = a + b
elif c =="-":
    o = a - b
elif c == "*":
    o = a * b
elif c =="/":
    o = a / b
print(str(a) + " " + c + " " + str(b) + " = " + str(o))

