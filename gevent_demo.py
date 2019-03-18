from gevent import monkey; monkey.patch_socket()
import os
import time
import gevent
import threading


def foo(n):
    print '[{}]Process {} - Thread {}'.format(time.time(), os.getpid(), threading.current_thread().ident)
    gevent.sleep(n) 


if __name__ == '__main__':
    t_start = time.time()
    g1 = gevent.spawn(foo, 1)
    g2 = gevent.spawn(foo, 2)
    g3 = gevent.spawn(foo, 3)
    g1.join()
    g2.join()
    g3.join()
    t_end = time.time()
    print(t_end - t_start)
