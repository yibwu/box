import time
import random


class TokenBucket():
    
    def __init__(self, rate, capability):
        self.rate = rate
        self.capability = capability
        self._current_amount = 0
        self._last_consume_time = time.time()

    def consume(self, token_amount):
        increment = (time.time() - self._last_consume_time) * self.rate
        self._current_amount = min(self._current_amount + increment, self.capability)
        print('token_amount: %s, _current_amount: %s' % (token_amount, self._current_amount))
        if token_amount > self._current_amount:
            return False
        else:
            self._current_amount -= token_amount
            self._last_consume_time = time.time()
            return True


if __name__ == '__main__':
    tb = TokenBucket(50, 100)
    for n in [10, 20, 50, 100]:
        ret = tb.consume(n)
        print(n, ret)
        time.sleep(random.random())
