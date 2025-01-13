from time import time
import asyncio

async def get_pages(site_name):
    if site_name == 'API':                              # Из-за того что нам плевать на всё кроме API, нет необходимости ждать остальные функции
        await asyncio.sleep(0.1)                                                    # А значит как только будет получена вся нужная инфа с API программа выведет результат
    else:                                                                                                               #  и завершит работу, не ожидая выполнения других функций
        await asyncio.sleep(1.5)
    print(f'Got pages for {site_name}')
    return range(1,4)

async def get_page_data(site_name, page):
    await asyncio.sleep(1)
    return f'Data from page {page} ({site_name})'

async def parsing(site_name):
    all_data = []
    pages = await get_pages(site_name)
    for page in pages:
        data = await get_page_data(site_name, page)
        print(data)
        all_data.append(data)
    return all_data                                                     # список отсортирован в порядке вызова функций (а не их завершения)
start = time()
func_list = [asyncio.ensure_future(parsing('Site_1')),                  # ensure_future- гарантирует вызов, и не смиотря на то, что сами функции не переданы в run_until_complete,
             asyncio.ensure_future(parsing('Site_2')),                                              # они будут исполнятся
             asyncio.ensure_future(parsing('Site_3'))]



event_loop = asyncio.get_event_loop()
result = event_loop.run_until_complete(parsing('API'))          # можно передать чисто одну функцию, а не список, тогда именно она будет результатом
print(result)                                                               # !!! Чаще всего такой способ передачи аргументов в event_loop будет считаться ОШИБОЧНЫМ
event_loop.close()

print(time() - start)