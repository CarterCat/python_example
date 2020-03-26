import redis

r = redis.Redis(host="localhost", port=6379, db=0)


k = "foo"

r.zadd(k, {"a": 3}, incr=True)
r.zadd(k, {"b": 1}, incr=True)
r.zadd(k, {"c": 2}, incr=True)

r.zrange(k, 0, -1, withscores=True)
r.zrevrange(k, 0, 2, withscores=True)


##

# hset

k = "bar"

r.hsetnx(k, 1, 0.1)
r.hsetnx(k, 2, 0.2)
r.hsetnx(k, 1, 0.3)

r.hgetall(k)
