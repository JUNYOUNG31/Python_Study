from typing import ContextManager
from django.db import models

# Create your models here.
class  Review(models.Model):
    movie_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.IntegerField()

    def __str__(self):
        return self.movie_title