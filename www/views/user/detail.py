from www.views.base import BaseView

class DetailView(BaseView):
    def get(self, request, user_id):
        self.render('/user/detail.html', data={})
