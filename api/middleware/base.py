#!/usr/bin/env python
# encoding=utf8
from tornado.web import RequestHandler

class BaseMiddleware(object):
    def prepare_request(self, handler):
        pass

    def prepare_response(self, handler):
        pass
