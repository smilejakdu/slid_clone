from django.db import models

class Product(models.Model):
    name        = models.CharField(max_length=200)
    price       = models.IntegerField()
    description = models.TextField()
    active      = models.BooleanField(default=True)

    class Meta:
        db_table = 'products'
