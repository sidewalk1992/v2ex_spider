#coding=utf-8

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

    def fetch_html(self, url):
        """获取页面 content """
        headers = {'User-Agent': ua.random}
        resp = requests.get(url, headers=headers, cookies=cookies)
        return resp.content

    def parse_topics_page(self, html):
        """解析话题列表页面"""
        soup = BeautifulSoup(html, 'lxml')
        for topic in soup.find_all('div', class_='cell item'):
            item_title = topic.find(class_='item_title')
            topic_info = topic.find(class_='topic_info')
            url = '%s%s' % (self.homepage, item_title.a.get('href').split('#')[0])
            title = item_title.a.text
            author = topic_info.find('strong').a.text
            entity = session.query(Topic).filter_by(url=url).first()
            if not entity:
                t = Topic(url=url, author=author, title=title)
                t.save()
                logger.info(t)
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

    def main(self):
        urls = ['{homepage}/recent?p={index}'.format(homepage=self.homepage, index=i) for i in range(1, 14692)]  # 14692
        for url in urls:
            html = self.fetch_html(url)
            self.parse_topics_page(html)


if __name__ == '__main__':
    v2ex = V2exSpider()
    v2ex.main()

