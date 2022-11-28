#!/bin/python3
import uuid
from datetime import datetime
"""Creating BaseModel class"""
DATETIME = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """my class"""
    def __init__(self, *args, **kwargs):
        """Initialization of new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     DATETIME)
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     DATETIME)
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """ printing of string representation"""
        class_name = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(class_name, self.id, self.__dict__)

    def save(self):
        """updating updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """initialization of dictionary"""
        dic = {}
        dic.update(self.__dict__)
        dic['__class__'] = (str(type(self)).split('.')[-1]).split('\'')[0]
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
