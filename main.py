"""Simple CI App Example
This is an initial exercise in creating a simple CI/CD workflow, it may develop
into an actual working website if i can find some interesting purpose.
Expect some street art photo's or something.
"""
import os
import re
import secrets
import datetime
from jinja2 import TemplateNotFound
from flask import Flask, render_template, request, redirect, session, url_for, abort

try:
    from google.cloud import datastore
except ImportError:  # pragma: no cover - optional cloud dependency
    datastore = None

try:
    from google.cloud import ndb
except ImportError:  # pragma: no cover - optional cloud dependency
    ndb = None

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-me')

datastore_client = None
if datastore is not None:
    try:
        datastore_client = datastore.Client()
    except Exception:
        datastore_client = None

LOCAL_VISIT_STORE = []
LOCAL_CONTACT_STORE = []


def generate_csrf_token():
    if 'csrf_token' not in session:
        session['csrf_token'] = secrets.token_hex(32)
    return session['csrf_token']


def is_valid_email(value):
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", value or ''))


def get_form_error(payload):
    name = (payload.get('name') or '').strip()
    email = (payload.get('email') or '').strip()
    email2 = (payload.get('email2') or '').strip()
    comment = (payload.get('comment') or '').strip()

    if not name or len(name) < 2:
        return 'Please enter your name.'
    if not is_valid_email(email):
        return 'Please enter a valid email address.'
    if email != email2:
        return 'The email addresses do not match.'
    if not comment or len(comment) < 10:
        return 'Please add a longer comment or question.'
    return None

@app.route('/')
def index():
    # Store the current access time in Datastore when a valid GCP config is available.
    if datastore_client is not None:
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
    return render_template('info.html', csrf_token=generate_csrf_token())

if ndb is not None:
    class Contact(ndb.Model):
        name = ndb.StringProperty()
        email = ndb.StringProperty()
        comment = ndb.StringProperty()
else:
    class Contact:
        def __init__(self, name, email, comment):
            self.name = name
            self.email = email
            self.comment = comment

        def put(self):
            LOCAL_CONTACT_STORE.append({
                'name': self.name,
                'email': self.email,
                'comment': self.comment,
            })

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        submitted_token = request.form.get('csrf_token', '')
        session_token = session.get('csrf_token', '')

        if not submitted_token or submitted_token != session_token:
            return render_template('form_failed.html', error='CSRF validation failed. Please try again.'), 400

        form_data = request.form.to_dict()
        validation_error = get_form_error(form_data)
        if validation_error:
            return render_template('form_failed.html', error=validation_error), 400

        try:
            if ndb is not None and datastore_client is not None:
                client = ndb.Client()
                with client.context():
                    contact = Contact(
                        name=form_data['name'].strip(),
                        email=form_data['email'].strip(),
                        comment=form_data['comment'].strip(),
                    )
                    contact.put()
            else:
                Contact(
                    name=form_data['name'].strip(),
                    email=form_data['email'].strip(),
                    comment=form_data['comment'].strip(),
                ).put()
        except Exception:
            app.logger.exception('Failed to save contact form submission')
            return render_template('form_failed.html', error='Unable to save your message right now. Please try again.'), 500

        session.pop('csrf_token', None)
        return redirect(url_for('html_page', page_name='confirmation.html'))

    return render_template('form_failed.html', error='This form requires a POST request.'), 405

@app.route('/<string:page_name>')
def html_page(page_name):
    try:
        return render_template(page_name)
    except TemplateNotFound:
        abort(404)


def store_time(dt):
    if datastore_client is not None:
        try:
            entity = datastore.Entity(key=datastore_client.key('visit'))
            entity.update({
                'timestamp': dt
            })
            datastore_client.put(entity)
            return
        except Exception:
            app.logger.warning('Datastore unavailable; skipping visit timestamp write.', exc_info=True)

    LOCAL_VISIT_STORE.append(dt)


def fetch_times(limit):
    if datastore_client is not None:
        try:
            query = datastore_client.query(kind='visit')
            query.order = ['-timestamp']
            times = query.fetch(limit=limit)
            return times
        except Exception:
            app.logger.warning('Datastore unavailable; returning empty visit list.', exc_info=True)

    ordered = sorted(LOCAL_VISIT_STORE, reverse=True)
    return ordered[:limit]


if __name__ == '__main__':
    host = os.getenv('HOST', '127.0.0.1')
    port = int(os.getenv('PORT', '8080'))
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 't']
    app.run(host=host, port=port, debug=debug_mode)
