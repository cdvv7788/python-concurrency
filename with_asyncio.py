from concurrent.futures import ProcessPoolExecutor
from wait import asyncio_slow_process, slow_process
import asyncio
import threading

@asyncio.coroutine
def main_coroutine():
    for i in range(0,10):
        print("Calling something that takes time to execute")
        yield from asyncio_slow_process()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_coroutine())
