from django.db import models
from user.models import User

class Folder(models.Model): 
    parent_idx  = models.CharField(max_length=100 , null=True)
    folder_name = models.CharField(max_length=100)
    depth_idx   = models.IntegerField(null=True)
    trash_bool  = models.BooleanField(default=False)
    user        = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'folder'
