


import redis

r = redis.Redis(host='localhost', port=6379, db=0)


# r.set('foo', 'bar')

# r.get('foo')
import time

key = "foo"
if r.set(key, 1, ex=1000, nx=True):
    try:
        print("execute")
        # time.sleep(1000)
        # import pdb
        # pdb.set_trace()
        raise 'abc'
    finally:
        r.delete('foo')
else:
    print("not execute")



import time

key = "foo"
if r.set(key, 1, ex=1000, nx=True):
    try:
        print("execute")
    finally:
        r.delete('foo')
else:
    print("not execute")





#-----
@app.task(queue="auction_start_worker")
def lane_start_worker(lane_id):
    key = redis_lane_start_lock_key % (lane_id,)
    if redis.set(key, 1, ex=10, nx=True):
        try:
            bid_runtime_service.start(lane_id)
        finally:
            redis.delete(key)

