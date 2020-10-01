#!/usr/bin/env python3
''' '''
from uuid import uuid4
from datetime import datetime

time_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel():
    ''' '''
    id = ''
    created_at = ''
    updated_at = ''

    def __init__(self, *args, **kwargs):
        ''' '''
        if kwargs:
            for key, val in kwargs.items():
                if key != '__class__':
                    setattr(self, key, val)
            if kwargs.get('created_at') and type(self.created_at) is str:
                self.created_at = datetime.strptime(
                    kwargs['created_at'], time_format)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get('updated_at') and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(
                    kwargs['updated_at'], time_format)
            else:
                self.updated_at = datetime.utcnow()
            if not kwargs.get('id'):
                self.id = str(uuid4())
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.utcnow()

    def __str__(self):
        """String representation of the Base model"""
        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        from models import storage
        self.updated_at = datetime.utcnow()
        storage.save(self)

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        print('""""""""\n', new_dict, '\n@@@@@@@@@@@@@@@@')
        if 'created_at' in new_dict:
            new_dict['created_at'] = new_dict['created_at'].strftime(
                time_format)
        if 'updated_at' in new_dict:
            new_dict['updated_at'] = new_dict['updated_at'].strftime(
                time_format)
        new_dict['_class_'] = self.__class__.__name__

        return new_dict


if __name__ == "__main__":
    pass
