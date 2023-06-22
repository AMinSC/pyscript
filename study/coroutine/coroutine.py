import asyncio

async def coroutine1():
    print("coro1 first entry point")
    await asyncio.sleep(1)
    print("coro1 second entry point")

async def coroutine2():
    print("coro2 first entry point")
    await asyncio.sleep(1)
    print("coro2 second entry point")

async def main():
    task1 = asyncio.create_task(coroutine1())
    task2 = asyncio.create_task(coroutine2())
    await task1
    await task2

asyncio.run(main())
