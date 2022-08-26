from turtle import title
from django.db import models

class Post(models.Model):
    title = models.CharField( max_length=50)
    content = models.TextField(default="no_content")
    thumbnail = models.TextField(default="no_thumbnail")
    created_at = models.DateTimeField( auto_now_add=True)


    def __str__(self):
        return str(self.id) + "-" + self.title  + "-" + self.thumbnail

