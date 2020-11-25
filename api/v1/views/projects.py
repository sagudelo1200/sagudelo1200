#!/usr/bin/python3
"""
Projects section of API DashFolio
"""
from flask import jsonify, request, abort
import requests
from api.v1.views import app_views
from models import storage
from models.project import Project

strict_slashes = {'strict_slashes': False}


@app_views.route('/projects', methods=['GET'], **strict_slashes)
def projects():
    ''' projects list
    Response:
      dict:
        description: dict of projects'''
    projects = storage.all(Project)
    return jsonify(**projects), 200


@app_views.route('/projects/<id>', methods=['GET'], **strict_slashes)
def get_project(id):
    ''' get project
    Response:
      dict:
        description: dict of specific project by id'''
    project = storage.get(Project, id)

    status = 404 if project.get('error') else 200

    return jsonify(project), status


@app_views.route('/projects/<id>', methods=['PUT'], **strict_slashes)
def put_project(id):
    '''  '''
    if not request.get_json():
        abort(400, description="Invalid JSON")

    project = storage.get(Project, id)

    return jsonify(project)
