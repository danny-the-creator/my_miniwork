from time import time
import asyncio

# Эти функции не передавались в event_loop, однако они были вызванны в другой функции (которая уже была в event_loop) и работали коректно
async def get_pages(site_name):
    await asyncio.sleep(0.5)
    print(f'Got pages for {site_name}')
    return range(1,4)

async def get_page_data(site_name, page):
    await asyncio.sleep(1)
    return f'Data from page {page} ({site_name})'

async def parsing(site_name):
    all_data = []
    pages = await get_pages(site_name)                                      # !! Функции, начинающиеся с async вызываются с помощью await
    for page in pages:
        data = await get_page_data(site_name, page)
        all_data.append(data)
    return all_data
start = time()
func_list = [asyncio.ensure_future(parsing('Site_1')),
             asyncio.ensure_future(parsing('Site_2')),
             asyncio.ensure_future(parsing('Site_3'))]


event_loop = asyncio.get_event_loop()
result = event_loop.run_until_complete(asyncio.gather(*func_list))          # подобные функции тоже могут возвращать значения и их можно присвоить переменной
print(result)
event_loop.close()

print(time() - start)