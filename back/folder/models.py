from django.db   import models
from user.models import User

class Folder(models.Model):
    name        = models.CharField(max_length=100)
    depth_idx   = models.IntegerField(null=True)
    trash_bool  = models.BooleanField(default=False)
    folder_path = models.ForeignKey('self' , on_delete=models.CASCADE , null=True)
    user        = models.ForeignKey(User , on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'folders'
