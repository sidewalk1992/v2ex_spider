[program:celery]
directory = /root/projects/v2ex_spider
command = celery worker -A tasks -P gevent -c 1000 -l info
stdout_logfile = /var/log/v2ex_spider/celery.log
stderr_logfile = /var/log/v2ex_spider/celery_error.log

[program:celery_beat]
directory = /root/projects/v2ex_spider
command = celery beat -A tasks -l info
stdout_logfile = /var/log/v2ex_spider/celery_beat.log
stderr_logfile = /var/log/v2ex_spider/celery_beat_error.log

[program:celery_flower]
directory = /root/projects/v2ex_spider
command = flower -A tasks --broker=redis://18.219.158.239:6379//
stdout_logfile = /var/log/v2ex_spider/celery_flower.log
stderr_logfile = /var/log/v2ex_spider/celery_flower_error.log
