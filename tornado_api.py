import os

import tornado.web
import tornado.gen
import tornado.ioloop
import tornado.options

from db import session, Topic


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        offset = self.get_argument('offset')
        limit = self.get_argument('limit', 10)

        entities = session.query(Topic).offset(offset).limit(limit).all()
        data = [e.to_dict() for e in entities]

        self.write({'success': True, 'msg': '', 'data': data})


if __name__ == '__main__':
    tornado.options.options.logging = 'debug'
    tornado.options.parse_command_line()
    settings = {
        'template_path': os.path.join(os.path.dirname(__name__), 'templates'),
        'static_path': os.path.join(os.path.dirname(__file__) , "static"),
        'debug': True
    }
    application = tornado.web.Application([
        (r'/', IndexHandler),
    ], **settings)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
