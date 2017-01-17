#!/usr/bin/env python
# encoding=utf8
from const import UserType
from core.logic import Application
from exception import AuthorityException
from glob import GlobalString
from www.views.base import BaseView


class ListView(BaseView):
    def get(self, request):
        user = request.user
        if user.type != UserType.Provider:
            err_msg = GlobalString.find('error_user_type_to_claim')
            raise AuthorityException(err_msg)

        provider_info = user.provider()
        app_obj_list = Application.filter(provider_id=provider_info['id'])
        app_dict_list = [a.info() for a in app_obj_list]
        self.render('/index.html', data=app_dict_list)
