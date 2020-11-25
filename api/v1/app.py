#!/usr/bin/env python3
''' DashFolio '''
from models import storage
from api.v1.views import app_views
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from
from os import environ

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
app.config['SWAGGER'] = {
    'title': 'DashFolio API - Santiago Agudelo',
    'uiversion': 1
}
strict_slashes = {'strict_slashes': False}

CORS(app, resources={r'/api/v1/*': {'origins': '*'}})
Swagger(app)


@app.errorhandler(404)
def not_found(e):
    ''' error 404
    Response:
      404:
        description: resourse not found.'''
    return jsonify({'error': "Resourse not found."}), 404


if __name__ == "__main__":
    ''' Main Function - Entry Point API '''
    host = environ.get('DASHFOLIO_API_HOST', '0.0.0.0')
    port = environ.get('DASHFOLIO_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True, debug=True)
