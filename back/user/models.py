from django.db import models

class User(models.Model): 
    email    = models.EmailField(max_length=250)
    password = models.CharField(max_length=250, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

    class Meta():
        db_table = 'users'
