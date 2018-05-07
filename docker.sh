#!/bin/bash

if [ $# != 1 ]; then
    echo "error command."
elif [ $1 == "build" ]; then
    echo "building..."
    docker build -t v2ex_spider .
elif [ $1 == "run" ]; then
    docker run -d \
        -t \
        --name v2ex_spider \
        v2ex_spider \
        bash
elif [ $1 == "enter" ]; then
    docker exec -it v2ex_spider bash
else
    echo "error command."
fi
