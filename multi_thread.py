import time
import threading


count = 10000
lock = threading.Lock()


def incr(n):
    global count
    for _ in range(n):
        lock.acquire()
        count += 1
        lock.release()


def decr(n):
    global count
    for _ in range(n):
        lock.acquire()
        count -= 1
        lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=incr, args=(10000,))
    t2 = threading.Thread(target=decr, args=(10000,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(count)
