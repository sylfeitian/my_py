import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(say_after(10, 'hello'))
        task2 = tg.create_task(say_after(3, 'world'))
        task3 = tg.create_task(say_after(5, 'nihao'))
    
        print(f'started at {time.strftime("%X")}')
    
    print(f"finished at {time.strftime('%X')}")
    
asyncio.run(main())