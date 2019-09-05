import time
import redis


class RateLimit:
    """ simple rate limit implemented by Redis """
    
    def __init__(self, redis_client, max_retry_times, expire_time):
        self.redis_client = redis_client
        self.max_retry_times = max_retry_times
        self.expire_time = expire_time

    def check(self, key):
        count = self.redis_client.incrby(key, 1)
        if count == 1:
            # which means the key doesn't exist before
            self.redis_client.expire(key, self.expire_time)
        return True if count <= self.max_retry_times else False
        

if __name__ == '__main__':
    r = redis.Redis(host='localhost', port=6379, db=0)
    rate_limit = RateLimit(r, 3, 5)
    key = 'test'
    for i in range(4):
        print(rate_limit.check(key))
        time.sleep(1)
