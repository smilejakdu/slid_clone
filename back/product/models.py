from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price        = models.IntegerField()
    description  = models.TextField()
    active       = models.BooleanField(default=True)

    class Meta:
        db_table = 'products'
