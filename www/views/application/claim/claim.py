#!/usr/bin/env python
# encoding=utf8
from const import UserType
from core.logic import Application
from exception import AuthorityException
from glob import GlobalString
from www.views.base import BaseView

class ClaimView(BaseView):
    def get(self, request, application_id):
        user = request.user
        if user.type != UserType.PROVIDER:
            err_msg = GlobalString.find('error_user_type_to_claim')
            raise AuthorityException(err_msg)

        provider_info = user.provider()
        app_obj = Application(application_id)
        app_obj.claim(provider_info['id'])
        self.render('/index.html', data={})
