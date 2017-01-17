#!/usr/bin/env python
# encoding=utf8
from www.views.base import BaseView
from core.logic import Application


class ApplyView(BaseView):
    def get(self, request):
        args = {}
        app_obj = Application.create(**args)
        self.render('/index.html', data=app_obj)
