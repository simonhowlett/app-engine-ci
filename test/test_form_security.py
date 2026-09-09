import unittest

from main import app


class FormSecurityTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()

    def test_homepage_loads_without_datastore_credentials(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Street Art', response.get_data(as_text=True))

    def test_favicon_request_is_not_treated_as_template(self):
        response = self.client.get('/favicon.ico')
        self.assertEqual(response.status_code, 404)

    def test_post_without_csrf_is_rejected(self):
        response = self.client.post(
            '/submit_form',
            data={
                'name': 'Tester',
                'email': 'tester@example.com',
                'email2': 'tester@example.com',
                'comment': 'Hello world',
            },
            follow_redirects=False,
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn('CSRF', response.get_data(as_text=True))

    def test_invalid_email_is_rejected(self):
        with self.client.session_transaction() as session:
            session['csrf_token'] = 'valid-token-for-test'

        response = self.client.post(
            '/submit_form',
            data={
                'csrf_token': 'valid-token-for-test',
                'name': 'Tester',
                'email': 'not-an-email',
                'email2': 'not-an-email',
                'comment': 'Hello world',
            },
            follow_redirects=False,
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn('email', response.get_data(as_text=True).lower())


if __name__ == '__main__':
    unittest.main()
