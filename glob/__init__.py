#!/usr/bin/env python
# encoding=utf8
from cn import CN
from en import EN

class GlobalString(object):
    def __init__(self, language):
        self._language = language
        self._language_instance = eval('%s()'%language)

    def find(self, key):
        return self._language_instance.attr(key)
