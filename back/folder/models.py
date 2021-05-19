from django.db   import models
from user.models import User

class Folder(models.Model):
    name          = models.CharField(max_length=200)
    depth_idx     = models.IntegerField(default=0)
    trash_basket  = models.BooleanField(default=False)
    parent_folder = models.ForeignKey('Folder' ,on_delete=models.CASCADE, null=True )
    user          = models.ForeignKey(User , on_delete=models.CASCADE)
    created_at    = models.DateTimeField(auto_now_add=True)

    class Meta():
        db_table = 'folders'

