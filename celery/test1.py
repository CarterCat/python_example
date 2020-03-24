from celery import Celery

app = Celery(
    "test1", backend="redis://localhost:6379/11", broker="redis://localhost:6379/11"
)

app.conf.update(
    CELERYBEAT_SCHEDULE={"a": {"task": "test1.a", "schedule": 0.1, "args": ()}}
)


x = 1


@app.task
def a():
    global x
    x += 1
    print(f"x={x}")
