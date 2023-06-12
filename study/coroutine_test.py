import asyncio

async def task(name, time):
    print(f'Task {name} will run for {time} seconds.')
    await asyncio.sleep(time)
    print(f'Task {name} is complete.')

async def main():
    # Create the tasks
    tasks = [task('A', 2), task('B', 1), task('C', 3)]

    # Run the tasks
    await asyncio.gather(*tasks)

# Run the main function
asyncio.run(main())
