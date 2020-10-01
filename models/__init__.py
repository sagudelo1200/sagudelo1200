#!/usr/bin/env python3
'''
Initialize de models package
'''
from os import getenv

st = getenv('PORTFOLIO_TYPE_STORAGE')
storage = None

if st == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
elif st == 'fs':
    from models.engine.db_storage import FileStorage
    storage = FileStorage()
    storage = 'FS'

if not storage:
    print('PORTFOLIO_TYPE_STORAGE: Not valid or not found')
    exit(-1)
