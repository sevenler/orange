from base import BaseObject


class Application(BaseObject):
    def __init__(self, pk):
        super(Application, self).__init__(pk)

    def claim(self, provider_id):
        pass

    def confirm(self, user_id):
        pass

    def send_offer(self, user_id):
        pass

    def update(self, **kwargs):
        pass

    @classmethod
    def create(self, *kwargs):
        pass

