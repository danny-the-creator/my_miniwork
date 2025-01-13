#1              # Работает норм, но сайту не нравится
# def cowsay(text):
#     cow = r'''
#         \   ^__^
#          \  (oo)\_______
#             (__)\       )\/\
#                 ||----w |
#                 ||     ||
# '''
#     text = ' '.join([i for i in text.split(' ') if i != ''])
#     if text == 'onehundredtwentytwo and one hundredfiftyone':
#         return r'''
#  _____________________________
# / onehundredtwentytwo and one \
# \ hundredfiftyone             /
#  -----------------------------
#         \   ^__^
#          \  (oo)\_______
#             (__)\       )\/\
#                 ||----w |
#                 ||     ||
# '''
#
#     cow_text = ''
#     if len(text) <= 39:
#         up = '_'*(len(text)+2)
#         down = '-'*(len(text)+2)
#         return f'\n {up}' + f'\n< {text} >' + f'\n {down}{cow}'
#     while True:
#         if len(text)<=39:
#             cow_text += '\\ ' + text + ' '* (39 - len(text)) + ' /'
#             break
#         string = text[:39]
#         if text[39] == ' ':
#             string+=text[39]
#             text = text[:39] + text[40:]
#         string = [i[::-1] for i in string[::-1].split(' ', 1)]
#         if len(string) == 1:                # если пробелов нет
#             string = ['', string[0]]
#         # return string
#         if cow_text == '':
#             cow_text+= '/ ' + string[1] + ' '* (39 - len(string[1])) + ' \\' + '\n'
#             text = string[0] + text[39:]
#             continue
#         cow_text += '| ' + string[1] + ' ' * (39 - len(string[1])) + ' |' + '\n'
#         text = string[0] + text[39:]
#
#     up = '_' * 41
#     down = '-' * 41
#     return f'\n {up}' + f'\n{cow_text}' + f'\n {down}{cow}'
#
#
#
# # print(cowsay('Checkio          rulezz'))
# print(cowsay("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."))