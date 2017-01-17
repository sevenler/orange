#!/usr/bin/env python
# encoding=utf8
from tornado.web import url
from api.views import user

handlers = [
    url(r"/user/(?P<user_id>\w+)", user.DetailView, name='user.detail'),
    url(r"/user/(?P<user_id>\w+)/change/password/", user.ChangePasswordView, name='user.change_password'),
    url(r"/account/sign/up/", user.SignUpView, name='user.sign_up'),
    url(r"/account/sign/in/", user.SignInView, name='user.sign_in'),
]
