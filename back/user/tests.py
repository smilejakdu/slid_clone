from django.test import TestCase, Client
from user.models import User

import unittest
import bcrypt
import json

class UserTest(TestCase):

    def setUp(self):
        User.objects.create(
            email    = "test@gmail.com",
            password = bcrypt.hashpw("12345678".encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            active   = 1
            )

    def tearDown(self):
        User.objects.all().delete()

    def test_SignUpView_post_success(self):
        client = Client()
        user   = {
            'email'    : 'test_string@gmail.com',
            'password' : '12345678',
            'active'   : 1
        }

        response = client.post('/users/signup', json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code,201)

    def test_SignUpView_post_duplicated_email(self):
        client = Client()
        user = {
            'email'    : 'test@gmail.com',
            'password' : '12345678',
            'active'   : 1
        }
        response = client.post('/users/signup', json.dumps(user), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "EMAIL_EXISTS"})

    def test_SignUpView_post_invalid_email(self):
        client = Client()
        user = {
            'email'    : 'invalidemail.com',
            'password' : '12345678',
            'active'   : 1
        }
        response = client.post('/users/signup', json.dumps(user), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),{"message": "INVALID_EMAIL"})

    def test_SignUpView_post_key_error(self):
        client = Client()
        user = {
            'password' : '12345678',
            'active'   : 1
        }
        response = client.post('/users/signup', json.dumps(user), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),{"message": "KEY_ERROR"})
