from django.db import models
from accounts_main.models import CustomUser
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts', default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'board'