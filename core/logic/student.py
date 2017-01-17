from base import BaseObject
from core.models import Student as StudentModel

class Student(BaseObject):
    def __init__(self, pk, model=None):
        super(Student, self).__init__(pk)

        self._object = None
        self._model = model

    def info(self):
        self._confirm_object()

    def _confirm_object(self):
        if self._object == None:
            if self._model == None:
                self._model = StudentModel.get(self.id)
            obj = {
                'name': self._model['name'],
                'age': self._model['age'],
            }
            self._object = obj

    def update(self, **kwargs):
        student_dict = {
            'name': kwargs['name'],
            'age': kwargs['age'],
        }
        self._confirm_object()
        self._model.update(student_dict)
        session.add(student_model)
        session.commit()

    @classmethod
    def create(self, **kwargs):
        student_dict = {
            'name': kwargs['name'],
            'age': kwargs['age'],
        }
        student_model = StudentModel(student_dict)
        session.add(student_model)
        session.commit()
