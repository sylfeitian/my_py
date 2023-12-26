import asyncio


# 定义一个协程函数
async def my_coroutine():
    print("协程开始")
    await asyncio.sleep(1)  # 模拟耗时操作
    print("协程结束")


# 创建一个事件循环
loop = asyncio.get_event_loop()
# 在事件循环中运行协程
loop.run_until_complete(my_coroutine())
# 关闭事件循环
loop.close()
