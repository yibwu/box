def producer(consumer):
    consumer.send(None)
    for i in range(1, 11):
        print('producing: %s' % i)
        consumer.send(i)
    consumer.close()
        

def consumer():
    while True:
        n = (yield)
        print('consuming: %s' % n)
        

if __name__ == '__main__':
    c = consumer()
    producer(c)
