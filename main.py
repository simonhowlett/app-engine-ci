"""Simple CI App Example
This is an initial exercise in creating a simple CI/CD workflow, it may develop
into an actual working website if i can find some interesting purpose.
Expect some street art photo's or something.
"""
import os
from flask import Flask, render_template, request, redirect
import datetime
from google.cloud import datastore, ndb

# [START gae_python38_app]
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
datastore_client = datastore.Client()

@app.route('/')
def index():
    # Store the current access time in Datastore.
    store_time(datetime.datetime.now())
    return render_template('index.html')

@app.route('/image/')
def image():
    return render_template('image.html')

@app.route('/visit/')
def visit():
    #  Fetch the most recent 10 access times from Datastore.
    times = fetch_times(10)
    return render_template(
        'visit.html', times=times)

@app.route('/info/')
def info():
    return render_template('info.html')

class Contact(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    comment = ndb.StringProperty()

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            client = ndb.Client()
            with client.context():
                data = request.form.to_dict()
                print(data)
                contact = Contact(name=data['name'],
                                  email=data['email'],
                                  comment=data['comment'])
                contact.put()
        except:
            return render_template('form_failed.html')
        return redirect('confirmation.html')
    else:
        return render_template('form_failed.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def store_time(dt):
    entity = datastore.Entity(key=datastore_client.key('visit'))
    entity.update({
        'timestamp': dt
    })

    datastore_client.put(entity)

def fetch_times(limit):
    query = datastore_client.query(kind='visit')
    query.order = ['-timestamp']

    times = query.fetch(limit=limit)

    return times

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python38_app]
