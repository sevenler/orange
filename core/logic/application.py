from base import BaseObject
from core.models import session
from core.models import Application as ApplicationModel
from core.models import Student as StudentModel
from const import ApplicationStatus
from exception import ErrorStatusException
from string import String


class Application(BaseObject):
    def __init__(self, pk, model=None):
        super(Application, self).__init__(pk)
        self._object = None
        self._model = model
        self._student_obj = None

    def info(self):
        self._confirm_object()
        return self._object

    def _confirm_object(self):
        if self._object == None:
            if self._model == None:
                self._model = ApplicationModel.get(self.id)
            if self._student_obj == None:
                student_id = self._object['student_id']
                self._student_obj = Student.filter(id=student_id)

            student_info = self._student_obj.info()
            obj = {
                'name': self._model['name'],
                'status': self._model['status'],
                'student_name': student_info['name'],
                'student_age': student_info['age'],
            }
            self._object = obj


    def claim(self, provider_id):
        if self.status != ApplicationStatus.CLAIMED:
            e_m = String.find('error_application_status_to_claim')
            raise ErrorStatusException(e_m)
        else:
            self._update_application(status=ApplicationStatus.CLAIMED)

    def confirm(self, user_id):
        if self.status != ApplicationStatus.CLAIMED:
            e_m = String.find('error_application_status_to_confirm')
            raise ErrorStatusException(e_m)
        else:
            self._update_application(status=ApplicationStatus.CONFIRMED)

    def send_offer(self, user_id):
        if self.status != ApplicationStatus.CONFIRMED:
            e_m = String.find('error_application_status_to_send_offer')
            raise ErrorStatusException(e_m)
        else:
            self._update_application(status=ApplicationStatus.SENT)

    def status(self):
        return self._object['status']

    def update(self, **kwargs):
        self._update_student(**kwargs)
        self._update_application(**kwargs)

    def _update_student(self, **kwargs):
        keys = ['student_name', 'age']
        args = {key: kwargs[key] for key in keys if kwargs.__contains__(key)}
        if len(args) > 0:
            self._confirm_object()
            self._student_obj.update(**args)

    def _update_application(self, **kwargs):
        keys = ['name', 'major_id']
        args = {key: kwargs[key] for key in keys if kwargs.__contains__(key)}
        if len(args) > 0:
            self._confirm_object()
            self._model.update(**args)

    @classmethod
    def create(self, **kwargs):
        student_dict = {
            'name': kwargs['student_name'],
            'age': kwargs['age'],
        }
        student = Student.create(**student_dict)

        application_dict = {
            'name': kwargs['name'],
            'major_id': kwargs['major_id'],
        }
        application_model = ApplicationModel(application_dict)
        session.add(application_model)
        session.commit()

    @classmethod
    def filter(self, **kwargs, offset=0, count=30):
        app_model_list = ApplicationModel.filter_by(session=session, **kwargs).all()
        app_object_list = []
        start = offset * count
        end = (offset + 1) * count
        for item in app_model_list[start:end]:
            app_object_list.append(cls(item.id, model=item))
        return app_object_list
