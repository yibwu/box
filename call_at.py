import asyncio
import time


def callback(n, loop):
    print('callback with {0} at {1}'.format(n, loop.time()))


async def main(loop):
    now = loop.time()
    print('clock time: {0}'.format(time.time()))
    print('loop time: {0}'.format(now))

    print('register callbacks')
    loop.call_at(now + 0.2, callback, 1, loop)
    loop.call_at(now + 0.1, callback, 2, loop)
    loop.call_soon(callback, 3, loop)

    await asyncio.sleep(1)


event_loop = asyncio.get_event_loop()
try:
    print('entering event loop')
    event_loop.run_until_complete(main(event_loop))
finally:
    print('closing event loop')
    event_loop.close()
