from core.logic import Application
from www.views.base import BaseView

class ConfirmView(BaseView):
    def get(self, request, application_id):
        app_obj = Application(application_id)
        self.render('/application/confirm.html', data=app_obj)

    def post(self, request, application_id):
        app_obj = Application(application_id)
        app_obj.confirm(request.user.id)
        self.render('/application/confirm.html', data=app_obj)
