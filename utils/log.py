#coding=utf-8

import logging

# def get_logger():
#     logger = logging.getLogger(__name__)
#     logger.setLevel(logging.INFO)
#     logger.addHandler(handler)
#     return logger
# 
# handler = logging.FileHandler('logs/spider.log', encoding='utf-8')
# formatter = logging.Formatter('%(asctime)s: %(filename)s [line:%(lineno)d]: [%(levelname)s]: %(message)s')
# handler.setFormatter(formatter)
# logger = get_logger()


logging.basicConfig(datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO,
        format='%(asctime)s: %(filename)s [line:%(lineno)d]: [%(levelname)s]: %(message)s')
logger = logging.getLogger(__name__)
