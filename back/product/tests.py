from django.test    import TestCase, Client
from product.models import Product

import unittest
import bcrypt
import json

class UserTest(TestCase):

    def setUp(self):
        Product.objects.create(
            name        = "Basic",
            price       = 6700,
            description = "description test",
            active      = True
            )

    def tearDown(self):
        Product.objects.all().delete()

    def test_ProductView_post_success(self):
        client = Client()
        product   = {
            'name'        : 'Basic',
            'price'       : 6700,
            'description' : "description test",
            'active'      : True
        }

        response = client.post('/product', json.dumps(product), content_type='application/json')
        self.assertEqual(response.status_code,201)

