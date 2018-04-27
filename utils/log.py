#coding=utf-8

import logging

logging.basicConfig(filename='log', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO,
# logging.basicConfig(datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO,
        format='%(asctime)s: %(filename)s [line:%(lineno)d]: [%(levelname)s]: %(message)s')
logger = logging.getLogger(__name__)
