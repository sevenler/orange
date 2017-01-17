from core.logic import Application
from www.views.base import BaseView


class ApplyView(BaseView):
    def get(self, request):
        args = {}
        args['name'] = request.data['name']
        application = Application.create(**args)
        self.render("apply/index.html", data=application)

class ClaimListView(BaseView):
    def get(self, request):
        user = request.user
        application = Application.filter(provider_id=user.id)
        self.render("apply/index.html", data=application)

class Claim(BaseView):
    def get(self, request, application_id):
        user = request.user
        application = Application(application_id)
        application.claim(user.id)
        self.render("apply/index.html", data=application)
