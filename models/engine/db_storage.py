#!/usr/bin/env python3
'''Contains the class DBStorage'''
from os import getenv

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from models.project import Project

classes = {'Project': Project}
cred = getenv('PORTFOLIO_CREDENTIALS')


class DBStorage:
    ''' '''
    __engine = None
    __db = None

    def __init__(self):
        ''' '''
        if not cred:
            print('PORTFOLIO_CREDENTIALS: Invalid certificate or not found')
            exit(-1)

        app = credentials.Certificate(cred)
        self.__engine = firebase_admin.initialize_app(app)
        self.__db = firestore.client()

    def all(self, col=None):
        '''
        query on te current firestorage session
        '''
        data = {}

        for class_ in classes:
            if not col or col == class_ or col is classes[class_]:
                docs = self.__db.collection(class_).stream()
                for _doc in docs:
                    obj = _doc.to_dict()
                    obj['id'] = _doc.id
                    key = f'{obj.get("_class_")}.{_doc.id}'
                    obj['__class__'] = obj.get('_class_')
                    obj.pop('_class_')
                    data[key] = obj
        return data

    def get(self, col, id: str):
        ''' Get dic from id in col '''
        doc = {}

        try:
            if col.__name__ not in classes:
                raise AttributeError

            docs = self.__db.collection(col.__name__).stream()
            for _doc in docs:
                if id == _doc.id:
                    obj = _doc.to_dict()
                    obj['id'] = _doc.id
                    key = f'{obj.get("_class_")}.{_doc.id}'
                    obj['__class__'] = obj.get('_class_')
                    obj.pop('_class_')
                    doc[key] = obj
        except AttributeError:
            return {'db_error': 'Invalid collection'}
        if not doc:
            return {'error': 'non-existent document in collection'}
        return doc

    def save(self, doc=None, merge=False):
        ''' Save in firestorage '''
        if doc:
            col = doc.__class__.__name__
            data = doc.to_dict()
            del data['id']
            doc_ref = self.__db.collection(col).document(doc.id)

            doc_ref.set(data, merge=merge)
        else:
            print('EXIT')
            exit(-1)

    def exists(self, col, id):
        '''Validate if doc exists in firestore'''
        docs = self.__db.collection(col).stream()

        for _doc in docs:
            if _doc.id == id:
                return True
        return False


if __name__ == "__main__":
    db = DBStorage()

    print(db.all())
