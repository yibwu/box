"""
implement producer and consumer by generator
"""

def producer():
    i = 0
    stop = False 

    while True:
        print('producing %s item...' % i)
        yield i
        i += 1


def consumer(producer):
    for i in range(10):
        ret = next(producer)
        print('consuming %s item...' % ret)

    producer.close()
    print('finish produce and consume')
        

if __name__ == '__main__':
    p = producer()
    consumer(p)
