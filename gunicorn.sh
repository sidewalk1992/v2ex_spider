#!/bin/bash

PORT=8888

start(){
    gunicorn flask_api:app \
    --bind 0.0.0.0:${PORT} \
    --workers 4 \
    --worker-class gevent \
    --max-requests 100 \
    --access-logformat='%(L)s %(h)s %(l)s %(t)s "%(r)s" %(s)s %(b)s' \
    --access-logfile=logs/gunicorn.access.log \
    --error-logfile=logs/gunicorn.error.log \
    --log-level debug \
    --daemon
}

stop(){
    kill -9 `ps -ef | grep 'gunicorn' | grep "0.0.0.0:${PORT}" | awk '{if($3==1) print $2}'`
}

reload(){
    kill -HUP `ps -ef | grep 'gunicorn' | grep "0.0.0.0:${PORT}" | awk '{if($3==1) print $2}'`
}

case $1 in
    start)
        echo "*** gunicorn start ***"
        start
    ;;
    stop)
        echo "*** gunicorn stop ***"
        stop
    ;;
    reload)
        echo "*** gunicorn reload ***"
        reload
    ;;
    restart)
        echo "*** gunicorn restart ***"
        stop
        sleep 1
        start
    ;;
    *)
        echo "wrong command"
    ;;
esac

