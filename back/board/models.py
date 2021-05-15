from django.db import models
from folder.models import Folder
# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    trash_bool = models.BooleanField(default=False)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

    class Meta:
        db_table = 'boards'

