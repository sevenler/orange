from cn import CN
from en import EN

class String(object):
    def __init__(self, language):
        self._language = language
        self._language_string = exec(language)

    def find(self, key):
        return self._language_string.attr(key)
