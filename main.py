"""Simple CI App Example

This is an initial exercise in creating a simple CI/CD workflow, it may develop
into an actual working website if i can find some interesting purpose.
Expect some street art photo's or something.
"""

import os

from flask import Flask
from flask import render_template

# [START gae_python38_app]
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/info/')
def info():
    return render_template('info.html')


@app.route('/confirmation/', methods=['GET', 'POST'])
def confirmation():
    return render_template('confirmation.html')


@app.route('/image/')
def image():
    return render_template('image.html')


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python38_app]
