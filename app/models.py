from turtle import title
from django.db import models

class Post(models.Model):
    title = models.CharField( max_length=50)
    content = models.TextField
    thumbnail = models.TextField
    created_at = models.DateTimeField( auto_now_add=True)


def __str__(self):
    return str(self.id) + "-" + self.title

