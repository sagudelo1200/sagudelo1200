#!/usr/bin/python3
"""
Index of API DashFolio
"""
from flask import jsonify
from api.v1.views import app_views

strict_slashes = {'strict_slashes': False}


@app_views.route('/status', methods=['GET'], **strict_slashes)
def status():
    ''' status API
    Response:
      OK:
        description: API WORKING'''
    return jsonify({'status': 'Developing...'})
