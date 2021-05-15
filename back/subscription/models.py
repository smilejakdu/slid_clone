from django.db import models
from user.models import User
from product.models import Product

class Subscription(models.Model):
    start_date          = models.DateTimeField(auto_now_add=True)
    end_date            = models.DateTimeField(auto_now_add=True)
    subscription_status = models.CharField(max_length=100 , null=True)
    user                = models.ForeignKey(User , on_delete=models.CASCADE)
    product             = models.ForeignKey(Product , on_delete=models.CASCADE)

    class Meta:
        db_table = 'subscriptions'
