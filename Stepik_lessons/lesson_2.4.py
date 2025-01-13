# text = '''First line
# Second line
# Third line'''
# print(text.splitlines())            # Удобный способ разбивать строку по строкам

# Файлы .txt являются итерируемыми объектоми и итерация происходит построчно
# file = open(...)
# for line in file:                   # Поэтому мы можем выводить файл при помощи цикла for
#     print(line)

# with open(...) as f, open(...) as file:             # !!! метод with поддерживает множественное открытие фалов (их можно перечислить через запятую)
#     pass

# Program
# with open('text.txt', 'w') as to_file, open(r'C:\Users\danny\Downloads\dataset_24465_4.txt') as from_file:
#     text = from_file.read().splitlines()
#     text = text[::-1]
#     new_text = '\n'.join(text)
#     to_file.write(new_text)

# !!! OS
# import os

# print(os.listdir(r'C:'))        # Просматривает всё в указанной папке (если не указать путь рассматривается текущая папка)
# print(os.path.exists('main.py'))        # Проверяет имеется-ли такой файл в текущей папке (можно указать и путь по идее)
# print(os.path.abspath('main.py'))       # Абсолютный путь до указанного файла или папки
#
# os.chdir(r'C:\Users\danny\Downloads')           # Позволяет сменить текущую директорию (папку, которая рассматривается по умолчанию, как если бы этот код был в той папке)

# !!! os.walk(                           Проходит рекурсивно по всем папкам и подпапкам в текущей директории
# for curent_dir, all_dirs, all_files in os.walk('D:\\'):             # !!! Сам объект os.walk() является генератором со всеми вытекающими
#     print(f'Текущая директория: {curent_dir}\nВсе здешние папки: {all_dirs}\nВсе здешние файлы: {all_files}')           # Проходим через все папки и файлы на диске D:\\
#     print()

# Final Program
# import os
# with open('text.txt', 'w') as file:
#     for curent_dir, all_dirs, all_files in os.walk(r'C:\Users\danny\Downloads'):
#         for f in all_files:
#             if f[-3:] == '.py':
#                 file.write(curent_dir.replace('C:\\Users\\danny\\Downloads\\','') + '\n')
#                 break