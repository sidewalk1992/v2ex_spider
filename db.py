#coding=utf-8

import datetime

from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, mapper

from conf import username, password, host, db

engine = create_engine("mysql+pymysql://{username}:{password}@{host}{db}?charset=utf8".\
    format(username=username, password=password, host=host, db=db))
base = declarative_base(engine)
Session = sessionmaker(bind=engine)
session = Session()


class Topic(base):
    __tablename__ = 'topic'
    id = Column(Integer, primary_key=True)
    url = Column(String(128), nullable=False)
    author = Column(String(128), nullable=False)
    title = Column(String(128), nullable=False)
    description = Column(Text)
    create_dt = Column(DateTime, default=datetime.datetime.now)

    __table_args__ = (
    # UniqueConstraint('author', 'title', name='uniq_author_title')
    UniqueConstraint('url', name='idx_url'),
    {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4',
    })

    def __repr__(self):
        return "<Topic(id={id}, title={title})>".format(id=self.id, title=self.title)

    def save(self):
        session.add(self)
        session.commit()

    def to_dict(self):
        return {
            'topic_id': self.id,
            'url': self.url,
            'title': self.title,
            'create_dt': str(self.create_dt),
        }


if __name__ == '__main__':
    base.metadata.drop_all()
    base.metadata.create_all()

