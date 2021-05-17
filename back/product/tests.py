from django.test    import TestCase, Client
from product.models import Product

import unittest
import bcrypt
import json

class UserTest(TestCase):

    def setUp(self):
        Product.objects.create(
            name        = "Basic_string",
            price       = 80,
            description = "description_test_string",
            active      = True
            )

    def tearDown(self):
        Product.objects.all().delete()

    def test_ProductView_post_success(self):
        client = Client()
        product   = {
            'name'        : 'Basic_string',
            'price'       : 80,
            'description' : "description_test_string",
            'active'      : True
        }

        response = client.post('/product', json.dumps(product), content_type='application/json')
        self.assertEqual(response.status_code,201)

    def test_ProductView_post_key_error(self):
        client = Client()
        user = {
            'name'  : 'Basic',
            'price' : 6700,
            'des'   : "description_test_error",
        }

        response = client.post('/product', json.dumps(user), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),{"message": "KEY_ERROR"})

    def test_ProductView_put_success(self):
        client = Client()
        Product.objects.create(
            name        = 'Basic_string',
            price       = 801,
            description = "description",
            active      = True
        )

        response = client.put('/product', json.dumps(product), content_type='application/json')
        self.assertEqual(response.status_code,200)

