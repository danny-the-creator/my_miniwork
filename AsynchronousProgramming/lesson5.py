from time import time
import asyncio
import functools                    # !!! Новый импорт

async def get_pages(site_name):
    await asyncio.sleep(0.5)
    print(f'Got pages for {site_name}')
    return range(1,4)

async def get_page_data(site_name, page, future):
    await asyncio.sleep(1)
    future.set_result(f'Data from page {page} ({site_name})')       # помещает результат в объект 'future', этот объект будет связующим звеном между event_loop и обычной функцией

async def parsing(site_name):
    pages = await get_pages(site_name)
    for page in pages:
        future = asyncio.Future()                                        # создание объекта future
        future.add_done_callback(upper_data)                             # применяем функцию 'upper_data' к объекту 'future' (! может принимать только один аргумент)
        future.add_done_callback(functools.partial(convert_data, 'lower'))              # благодаря 'partial', мы создаём новую функцию, в которой method уже установлен на lower
        future.add_done_callback(functools.partial(convert_data, 'capitalize'))     # это можно сделать и без callback-ов, другими функциями, но в случае их ошибки программа
                    # прекратит своё выполнение, в случае если ошибка в callback-е, программа будет продолжать работать и каждый раз будет выводить либо результат, либо ошибку
        await get_page_data(site_name, page, future)

def upper_data(future):                             # функция, которая будет применятся к каждой странице, кождого сайта
    print(future.result().upper())                                          # выводит текст большими буквами

def convert_data(method, future):                   # (Нельзя менять why?)
    result = future.result()
    print(getattr(result, method)())                  # применяет введённый метод к строке
start = time()
func_list = [asyncio.ensure_future(parsing('Site_1')),
             asyncio.ensure_future(parsing('Site_2')),
             asyncio.ensure_future(parsing('Site_3'))]


event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(asyncio.gather(*func_list))
event_loop.close()

print(time() - start)