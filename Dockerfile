FROM python

MAINTAINER Sidewalk <sidewalk0920@gmail.com>

WORKDIR /projects/v2ex_spider
# COPY . /projects/v2ex_spider
COPY requirements.txt /projects/v2ex_spider
RUN echo "Asia/Shanghai" > /etc/timezone \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && pip install -r requirements.txt
CMD ./gunicorn.sh start
# RUN apt update \ 
#     && apt install -y vim \ 
#     && rm -rf /var/lib/apt/lists/* \
#     && pip install -r requirements.txt
