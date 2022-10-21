import redis


class RedisQueue(object):

    def __init__(self, **redis_kwargs):

        self.rq = redis.Redis(**redis_kwargs)

    def size(self, key):  # get Redis Key lenghth
        return self.rq.llen(key)

    def isEmpty(self, key):  # check Redis key is Empty
        return self.size(key) == 0

    def put_data(self, key, element):
        self.rq.lpush(key, element)  # left push

    def get(self, key):
        element = self.rq.rpop(key, count=10000)  # key에서 count 만큼 data get
        return element
