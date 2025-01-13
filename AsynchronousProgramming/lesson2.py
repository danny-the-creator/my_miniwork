from time import time
from time import sleep
import asyncio

def loader(url):                                    # неасинхронная функция
    print(f'Load {url} at {time()-start}')

async def parsing(site_name):
    for page in range(3):
        await asyncio.sleep(1)
        if page == 0:
            sleep(2)                            # имитация работы программы
        print(site_name, page)

start = time()
func_list = [asyncio.ensure_future(parsing('Site_1')),
             asyncio.ensure_future(parsing('Site_2')),
             asyncio.ensure_future(parsing('Site_3'))]


event_loop = asyncio.get_event_loop()
event_loop.call_soon(loader, 'url1')                    # передаём неасинхронную функцию, которую нужно вызвать во время цикла обработки событий в ближайшее время
event_loop.call_later(2, loader, 'url2')                # вызовет функцию, через две секунды, !НО! только если все функции в цикле обработки событий будут в режиме ожидания
                                                            # выполняется через 7 секунд, а не через 2, потому что программа занята другими функциями и не может вызвать эту
now = event_loop.time()                                     # у этого модуля есть свой вариант time и он показывает текущее время в цикле обработки событий
event_loop.call_at(now+8, loader, 'url3')                   # вызывает функцию в указанное время (!!! Если программа завершиться до наступления указанного времени,
                                                                                                                                                # функция не будет выполнена)
event_loop.run_until_complete(asyncio.gather(*func_list))                                                                   # когда все 3 сопрограммы перейдут в режим ожидания
event_loop.call_soon(loader, 'url0')                    #! НЕ будет выполняться, так как event_loop уже завершён (функцию надо записывать до цикла обработки событий)
event_loop.close()

print(time() - start)