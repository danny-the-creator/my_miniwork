# !!! Параллельный запуск сопрограмм !!!
from time import time
import asyncio

async def get_pages(site_name):
    await asyncio.sleep(0.5)
    print(f'Got pages for {site_name}')
    return range(1,6)

async def get_page_data(site_name, page):
    if site_name == 'API':              #! имитация бага сервера, который выдал большую задержку, однако мы не хотим ожидать ответа от сломанного сайта, да ещё и целых 100 секунд
        delay = 100                                                                                     # Поэтому ниже мы установим ограничение на время выполнения
    else:
        delay = 1
    await asyncio.sleep(delay)
    return f'Data from page {page} ({site_name})'

async def parsing(site_name):
    pages = await get_pages(site_name)
    co_pages = []

    for page in pages:
        co_pages.append(get_page_data(site_name, page))     # вызов асинхронной функции создаёт корутину, которую мы потом добавляем в список

    #! Вместо цикла, который тормозит программу, теперь можно написать слудующее:
    for co_page in asyncio.as_completed(co_pages, timeout=3):      # as_completed - возвращает иттератор из всех переданных в него программ
                                            # timeout - выдаёт ошибку через 'n' секунд, если какие-то программы не были завершены (ограничивает общее время выполнения сопрограмм)
        try:
            data = await co_page                   # в первой иттерации запускаются все корутины, а дальше как только какая-то из них завершится, она будет возвращена в программу
            print(data)                    # несмотря на то, что мы передали 5 сайтов и 5 страниц (вместо 3 и 3), выполнение нашей программы сократилось до 1,5 (вместо 3)
                                                    # В среднем, при использовании наших входных данных, наша программа работает в 10 раз быстрее линейных
        except asyncio.TimeoutError:
            print('Время ожидания отклика сайта истекло')           # В случае, если появилась ошибка, страница будет проигнорированна и выведенно это сообщение
start = time()
func_list = [asyncio.ensure_future(parsing('Site_1')),
             asyncio.ensure_future(parsing('Site_2')),
             asyncio.ensure_future(parsing('Site_3')),
             asyncio.ensure_future(parsing('API')),
             asyncio.ensure_future(parsing('Game'))]

event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(asyncio.gather(*func_list))
event_loop.close()

print(time() - start)