def backup_copy(*args):
    import os
    import time
    import zipfile
    import re

    def zip(a):
        n = 0
        for folder, subfolder, files in os.walk(a):
            for file in files[::-1]:
                if bool(re.search(r'\bpng', file)) == True:
                    if n <= 50:
                        result.write(os.path.join(folder, file))
                        n += 1
                else:
                    result.write(os.path.join(folder, file))

    comment = ""
    if __name__ == '__main__':
        comment = input("Хотите что-то уточнить? ")
    # important_data, important_pictures = r'D:\Программирование', r'C:\Users\danny\Pictures\Screenshots'
    backup_place = r'D:\Резервное_копирование'                                # Путь к резервным копиям
    today = backup_place + os.sep + time.strftime("%d.%m.%Y")
    now = time.strftime('%H.%M')

    if not os.path.exists(today):
        os.mkdir(today)
        print("Kаталог успешно создан", today)
    if len(comment) == 0:
        zip_command = today + os.sep + now + ".zip"
    else:
        zip_command = today + os.sep + now + "_" + comment.replace(" ","_") + ".zip"

    result = zipfile.ZipFile(zip_command, 'w')
    for i in args:
        zip(i)

    result.close()
    if len(comment) == 0:
        print("Резервная копия успешна создана")
    else:
        print('Резервная копия с вашим комментарием: "{}" успешна создана'.format(comment))
if __name__ == '__main__':
    important_data, important_pictures = r'D:\Программирование\Python начало', r'C:\Users\danny\Pictures\Screenshots'
    backup_copy(important_data, important_pictures)