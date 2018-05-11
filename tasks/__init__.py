import time
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

from conf import celery_broker, celery_backend


app = Celery('v2ex_spider', broker=celery_broker, backend=celery_backend)
app.conf.timezone = 'Asia/Shanghai'
app.conf.task_time_limit = 30 * 60
app.conf.redis_max_connections = 100
app.conf.result_cache_max = 5000 # 存储n条任务结果
app.conf.worker_max_tasks_per_child = 1000 # 每个worker执行n次重启（资源释放问题）
app.conf.imports = ['spider']

app.conf.beat_schedule = {
    # 'add-every-30-seconds': {
    #     'task': 'tasks.add',
    #     'schedule': 30.0,
    #     # 'schedule': crontab(hour=7, minute=30, day_of_week=1),
    #     'args': (16, 16)
    # },
    'spider': {
        'task': 'spider.main',
        'schedule': crontab(minute=1, hour='*/1'),
        'args': None
    },
}


@app.task
def add(x, y):
    time.sleep(3)
    return x+y
