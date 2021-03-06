from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.title
