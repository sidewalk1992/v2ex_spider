#!/bin/bash

build(){
    echo "building..."
    docker build -t v2ex_spider .
}

run(){
    docker run -d \
            -t \
            --name v2ex_spider \
            -p 9999:9999 \
            -v `pwd`:/projects/v2ex_spider \
            v2ex_spider \
            bash
}

enter(){
    docker exec -it v2ex_spider bash
}

if [ $# != 1 ]; then
    echo "error command."
elif [ $1 == "build" ]; then
    build
elif [ $1 == "run" ]; then
    run
elif [ $1 == "enter" ]; then
    enter
elif [ $1 == "rebuild" ]; then
    docker rm -f v2ex_spider
    docker rmi v2ex_spider
    build
else
    echo "error command."
fi

