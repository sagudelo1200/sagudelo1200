#!/usr/bin/env python3
''' DashFolio Web '''
from flask import Flask, render_template, make_response
from os import getenv

app = Flask(__name__)
strict_slashes = {'strict_slashes': False}


@app.route('/', **strict_slashes)
def index():
    ''' index '''
    return render_template('index.html')


if __name__ == "__main__":
    ''' Main Function - Entry Point DashFolio Web '''
    host = getenv('DASHFOLIO_HOST', default='0.0.0.0')
    port = getenv('DASHFOLIO_PORT', default=3000)
    app.run(host=host, port=port, threaded=True, debug=True)
