#Asynchronous function
import asyncio
async def task1():
  print("Task 1 starts")
  await asyncio.sleep(2)
  print("Task 1 completed")

async def task2():
  print("Task 2 starts")
  await asyncio.sleep(2)
  print("Task 2 completed")


async def main():
    await asyncio.gather(task1(),task2())

asyncio.run(main())