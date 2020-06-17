# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Simple CI App Example

This is an initial exercise in creating a simple CI/CD workflow, it may develop
into an actual working website if i can find some interesting purpose. 
Expect some street art photo's or something.
"""
import logging
import os
# [START gae_python38_app]
from flask import Flask

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
# to run locally, run python main.py in the terminal
app = Flask(__name__)


@app.route('/')



def hello():
    """Return a friendly HTTP greeting."""
    return '''<html>
<title>Simon Howlett Test CI Pipeline</title>
    <head>
    <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-W66F3F1E6H"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-W66F3F1E6H');
</script>
    </head>
        <body>
        <table witdth='100%'border=0>
        <tr><td width='30%'><h1><center>
        <br />
        <br /><p class="content">
        Nothing to see here, yet...</p></center><h1></td></tr>
        </table>
        </body>
    </html>'''

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python38_app]
