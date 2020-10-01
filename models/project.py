#!/usr/bin/env python3
''' '''
from models.base_model import BaseModel
from models import storage


class Project(BaseModel):
    ''' representation of Project '''
    title = ''
    description = ''
    category = 0
    photo_url = ''

    def __init__(self, *args, **kwargs):
        ''' Initializes Project '''
        super().__init__(*args, **kwargs)
