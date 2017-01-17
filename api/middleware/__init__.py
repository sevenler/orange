#!/usr/bin/env python
# encoding=utf8
from parse_post_body import ParsePostBodyMiddleware

def get_all_middleware():
    return [ParsePostBodyMiddleware()]
