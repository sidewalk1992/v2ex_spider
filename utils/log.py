#coding=utf-8

import logging

formatter = logging.Formatter('%(asctime)s: %(filename)s [line:%(lineno)d]: [%(levelname)s]: %(message)s')
handler = logging.FileHandler('log.txt', encoding='utf-8')
handler.setFormatter(formatter)

# logging.basicConfig(filename='log', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO,
#         format='%(asctime)s: %(filename)s [line:%(lineno)d]: [%(levelname)s]: %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


