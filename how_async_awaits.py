import asyncio
import time

async def make_tea():
    print('Making tea')
    # time.sleep(2)
    await asyncio.sleep(2)
    return 'tea'

async def make_dosa():
    print('Making dosa')
    # time.sleep(5)
    await asyncio.sleep(5)
    return 'dosa'

async def main():
    start_time = time.time()
#    tea = asyncio.create_task(make_tea())
#    dosa = asyncio.create_task(make_dosa())
#    await tea
#    await dosa
    batch = asyncio.gather(make_tea(), make_dosa())
    tea, dosa = await batch
    print(f'Tea and dosa are ready in {time.time() - start_time} seconds')

if __name__ == '__main__':
        asyncio.run(main())
