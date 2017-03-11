from time import sleep
import gevent
import asyncio

def slow_process(n=2):
    """
    Sleeps n seconds
    """
    print('Sleeping {} seconds'.format(n))
    sleep(n)

@asyncio.coroutine
def asyncio_slow_process(n=2):
    """
    Sleeps n seconds. Compatible with asyncio
    """
    print('Sleeping {} seconds'.format(n))
    asyncio.sleep(n)

def gevent_slow_process(n=2):
    """
    Sleeps n seconds. Compatible with asyncio
    """
    print('Sleeping {} seconds'.format(n))
    gevent.sleep(n)
