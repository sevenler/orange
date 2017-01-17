#!/usr/bin/env python
# encoding=utf8
from www.views.base import BaseView
from core.logic import Application

class DetailView(BaseView):
    def get(self, request, application_id):
        app_obj = Application(application_id)
        app_dict = app_obj.info()
        self.render('/index.html', data=app_dict)
