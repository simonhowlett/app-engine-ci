"""Simple CI App Example

This is an initial exercise in creating a simple CI/CD workflow, it may develop
into an actual working website if i can find some interesting purpose. 
Expect some street art photo's or something.
"""

import os
# [START gae_python38_app]
from flask import Flask
from flask import render_template

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Creates the info page, and takes the last paramter as the URL and passes it
# into text.
@app.route('/info/')
@app.route('/info/<name>')
def hello(name=None):
    return render_template('info.html', name=name)

# Details Page
@app.route('/details')
def details():
    return 'Some Details'

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python38_app]
