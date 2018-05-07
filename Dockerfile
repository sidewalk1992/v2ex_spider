FROM python

MAINTAINER Sidewalk <sidewalk0920@gmail.com>

RUN mkdir -p /projects/v2ex_spider
WORKDIR /projects/v2ex_spider
COPY . /projects/v2ex_spider
RUN echo "Asia/Shanghai" > /etc/timezone \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && pip install -r requirements.txt
# RUN apt update \ 
#     && apt install -y vim \ 
#     && rm -rf /var/lib/apt/lists/* \
#     && pip install -r requirements.txt
