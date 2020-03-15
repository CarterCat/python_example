# celery beat -A tasks
# celery worker -A tasks --loglevel=info


from celery import Celery
from celery.schedules import crontab

app = Celery()


app.conf.beat_schedule = {
    # 'aaa': {
    #     'task': 'tasks.test',
    #     'schedule': 1.0,
    #     'args': (1,)
    # },
    # 'bbb': {
    #     'task': 'tasks.test',
    #     'schedule': 5.0,
    #     'args': ("foo",)
    # },
    'ccc': {
        'task': 'tasks.test2',
        'schedule': 0.1,
        'args': ()
    }
}

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(1.0, test.s(), name='add every 10')
#     sender.add_periodic_task(5.0, test.s(), expires=10)

@app.task
def test(a):
    print(a)

import time

@app.task
def test2():
    print(time.time())