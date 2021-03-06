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

    def test_SigninView_post_success(self):
        client = Client()
        sign_in_user = {
            "email"    : "test@gmail.com",
            "password" : "12345678"
        }

        response = client.post('/users/signin', json.dumps(sign_in_user), content_type='application/json')
        self.assertEqual(response.status_code, 200)


    def test_SigninView_post_password_incorret(self):
        client = Client()
        sign_in_user = {
            "email"    : "test@gmail.com",
            "password" : "incorret"
        }
        response = client.post('/users/signin', json.dumps(sign_in_user), content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(),{"message": "INVALID_PASSWORD"})


    def test_EmailSigninView_post_user_not_exists(self):
        client = Client()
        sign_in_user = {
            'email'    : 'notexists@gmail.com',
            'password' : '123456789',
        }
        response = client.post('/users/signin', json.dumps(sign_in_user), content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(),{"message": "INVALID_USER"})
