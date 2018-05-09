#coding=utf-8

import time
import traceback

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from sqlalchemy.exc import IntegrityError

from db import session, Topic
from utils.log import logger
from conf import cookies

ua = UserAgent()


class V2exSpider:
    def __init__(self):
        self.homepage = 'https://www.v2ex.com'
        self.existed_cnt = 0  # 已存在topic数目
        self.fail_cnt = 0  # 失败次数

    def fetch_html(self, url):
        """获取页面 content """
        headers = {'User-Agent': ua.random}
        resp = requests.get(url, headers=headers, cookies=cookies, timeout=10)
        if resp.status_code == 200:
            return resp.content
        else:
            logger.error('resp.status_code: %s' % resp.status_code)

    def parse_topics_page(self, html):
        """解析话题列表页面"""
        soup = BeautifulSoup(html, 'lxml')
        for topic in soup.find_all('div', class_='cell item'):
            item_title = topic.find(class_='item_title')
            topic_info = topic.find(class_='topic_info')
            url = '%s%s' % (self.homepage, item_title.a.get('href').split('#')[0])
            title = item_title.a.text
            author = topic_info.find('strong').a.text
            self.save(url, author, title)
            # 解析详情页
            # topic_html = self.fetch_html(url)
            # self.parse_topic_page(url, topic_html)

    def parse_topic_page(self, url, html):
        """解析话题详情页面"""
        soup = BeautifulSoup(html, 'lxml')
        author = soup.find('small', class_='gray').a.text
        title = soup.title.text.split(' - V2EX')[0]
        description = soup.find('div', class_='topic_content').text

        entity = session.query(Topic).filter_by(url=url).first()
        if not entity:
            t = Topic(url=url, author=author, title=title, description=description)
            t.save()
            logger.info(t)

    def save(self, url, author, title):
        entity = session.query(Topic).filter_by(url=url).first()
        if entity:
            logger.warning('topic已存在，id:%s' % entity.id)
            self.existed_cnt += 1
            return False
        else:
            t = Topic(url=url, author=author, title=title)
            t.save()
            logger.info(t)
            return True
        
    def main(self):
        urls = ['{homepage}/recent?p={index}'.format(homepage=self.homepage, index=i) for i in range(0, 14692)]  # 14692
        for url in urls:
            logger.info('Featching: %s' % url)
            try:
                html = self.fetch_html(url)
                self.parse_topics_page(html)
                self.fail_cnt = 0
            except:
                self.fail_cnt += 1
                logger.error(traceback.format_exc())
            finally:
                time.sleep(1)
                if self.fail_cnt > 30 or self.existed_cnt > 300:
                    break


if __name__ == '__main__':
    v2ex = V2exSpider()
    v2ex.main()

