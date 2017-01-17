#!/usr/bin/env python
# encoding=utf8
from tornado.web import url
from www.views import application, user

handlers = [
    url(r"/user/(?P<user_id>\w+)", user.DetailView, name='user.detail'),

    url(r"/application/apply/", application.ApplyView, name='application.apply'),
    url(r"/application/", application.ListView, name='application.list'),
    url(r"/application/claim/", application.ClaimListView, name='application.claim.list'),
    url(r"/application/(?P<application_id>\w+)", application.DetailView, name='application.detail'),
    url(r"/application/(?P<application_id>\w+)/claim/", application.ClaimView, name='application.claim'),
    url(r"/application/(?P<application_id>\w+)/confirm/", application.ConfirmView, name='application.confirm'),
]
