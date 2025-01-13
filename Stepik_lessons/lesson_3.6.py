# xml - это формат, который очень похож на html, но все элементы (<tag>...</tag>) мы придумываем сами
# элементы в 'xml' это теги вида <tag>...</tag>, при этом информация между текстом называется содержимым тега и может содержать в себе другие теги или просто текст
# теги также могут иметь другой вид: '<tag/>' (этот тег и открывается и закрывается одновременно)
# теги xml также могут содержать и некоторые Атрибуты (атрибуты - это пара ключ-значений, которые разделены при помощи '=' и значения всегда в кавычках)
# атрибуты помогают отличить два элемента с одинаковыми тегами
# <tag id="12">             В данном примере 'id' - это атрибут элемента

# В формате xml мы сами придумываем себе формат, теги, их атрибуты и всё остальное (поэтому нужно быть очень аккуратным с названиями, чтобы не запутаться в них)

# Так как элементы могут содержать другие элементы в данном формате, структуру 'xml' можно представить в виде древа


# !!! Нижеприведённый код не работает, он создан с целью объяснения функций библиотеки, но без создания самого xml файла
# from xml.etree import ElementTree                   # библиотека, позволяющая работать с 'xml' файлами
#
# xml = ElementTree.parse('file.xml')                 # Вместо 'file' должно быть название самого файла
#
# root = xml.getroot()                                # Выводит корень древа (элемент, в котором содержится всё остальное)
# print(root.text)                                    # Выводит текстовое содержимое элемента
# for child in root:
#     print(child.tag, child.attrib)                  # Таким образом можно перебрать всех детей главного элемента
#
# # ! В питоне все объекты и элементы xml имеют одинаковый класс: 'element'
#
# root.iter('tag')                                    # Из всего корня будут предоставлены только элементы с тегом 'tag' (но из всего корня из его детей, внуков, правнуков и тд)
    # root.findall('tag')                                 # Делает тоже самое, но переберает только прямых наследниках корня (его детей, но НЕ внуков и тд)
#
# xml.write("file1.xml")                              # Запишет наши данные в питоне (которые являются представлением xml) в xml file c указанным названием
#
# element.set('key', 'value')                         # добавление атрибута элементу
#
# new_tag = ElementTree.Element('new_tag')            # создание нового тега
# new_tag.text = 'Some additional information'        # добавление содержания этого тега
# root.append(new_tag)                                # перенос этого тега в элемент корня
#
# useless_tag = root.find('new_tag')                  # Находит недавно созданный тег в корне
# root.remove(useless_tag)                            # Удаляет лишний тег из элемента корня
#
# another_tag = ElementTree.SubElement(child, 'name')   # создание тега внутри елемента какого-то ребёнка (ветви дерева), имя тега : name
#
# tree = ElementTree.ElementTree(root)                # создание самого 'дерева' в которое передаётся корень (а в корне уже содержится вся информация)

# ! Пример file.xml
# <studentsList>
#     <student id='1'>
#         <firstName>Greg</firstName>
#         <lastName>Dean</lastName>
#         <certificate>True</certificate>
#         <scores>
#             <module1>70</module1>
#             <module2>80</module2>
#             <module3>90</module3>
#         </scores>
#     </student>
#     <student id='2'>
#         <firstName>Wirt</firstName>
#         <lastName>Wood</lastName>
#         <certificate>True</certificate>
#         <scores>
#             <module1>80</module1>
#             <module2>80.2</module2>
#             <module3>80</module3>
#         </scores>
#     </student>
# </studentsList>

# ! Перенос строк необязателен, он лишь упрощает чтение

# !!! Часто большая часть интернет трафика является плохо сформированной и нестабильной, это не влияет на работу сайтов, но затрудняет детальный разбор по 'дереву' (парсинг)
                                                                                          # тоесть мы не можем работать с РЕАЛЬНЫМИ html сайтами точно также как мы работали с xml
# Поэтому для работы с такими сайтами (в принципе со всеми html сайтами) существуют некоторые библиотеки: (beautifulsoup, lxml)

# from lxml import etree                              # библиотека lxml пытается вести себя точно также как и xml.ElementTree, но работает она, в частности, и с html
# import requests
#
# res = requests.get("http://docs.python.org/3/")     # обычный запрос на сайт (html)
#
# parser = etree.HTMLParser()                         # !!! позволяет работать с плохо сформированными данными, как с обычными (стирает косяки и упрощает жизнь)
#
# root = etree.fromstring(res.text, parser)           # передача данных в формате html в переменную (данные фильтруются и записываются в той же структуре, что и с xml,
#                                                                                                             # следовательно работать с ними можно точно также)
# # Нахождение всех ссылок на сайте при помощи 'HTMLParser'
# for element in root.iter("a"):                  # перебераем все 'поддеревья' в корне, у которых есть тег <a> (тоесть тот текст, что является ссылкой)
#     print(element.attrib)                       # выводит атрибуты всех элементов <a> (среди которых и находятся искомые ссылки)

# The Most Final Program Of All Final Programs
# from xml.etree import ElementTree
#
# result = {'red': 0,
#           'green': 0,
#           'blue': 0}
#
# def getchild(tree, level):
#     global result
#     child_list = tree.findall('cube')
#     for child in child_list:
#         result[child.attrib['color']] += level
#         getchild(tree=child, level=level+1)
#
# tree = ElementTree.fromstring(input())
#
# result[tree.attrib['color']]+=1
#
# getchild(tree, level=2)
#
# print(result['red'], result['green'], result['blue'])

# <cube color="blue">
#   <cube color="red">
#       <cube color="green"></cube>
#   </cube>
#   <cube color="red"></cube>
# </cube>

# Конец Курса!