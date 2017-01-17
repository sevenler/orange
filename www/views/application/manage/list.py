#!/usr/bin/env python
# encoding=utf8
from www.views.base import BaseView
from core.logic import Application

class ListView(BaseView):
    def get(self, request):
        status = request.GET['status']
        app_obj_list = Application.filter(status=status)
        app_dict_list = [a.info() for a in app_obj_list]
        self.render('/index.html', data=app_dict_list)
