#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from api.urls import handlers as api_handlers
from www.urls import handlers as www_handlers
from tornado.options import define, options
from config import ADDRESS_PORT

define("port", default=ADDRESS_PORT, help="run on the given port", type=int)

class Application(tornado.web.Application):
   def __init__(self):
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "www/templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )

        handlers = api_handlers + www_handlers
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
