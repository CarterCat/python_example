


import redis

r = redis.Redis(host='localhost', port=6379, db=0)


r.set('foo', 'bar')

r.get('foo')


if r.setnx('foo', 1):
    # do ....
    r.delete('foo')

