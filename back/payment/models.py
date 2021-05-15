from django.db import models
from user.models import User

# Create your models here.

class Payment(models.Model):
    pay_kind = models.CharField(max_length=200)
    pay_bank = models.CharField(max_length=200)
    pay_approval = models.CharField(max_length=200)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'payments'