from django.db import models

# Create your models here.
class movie_actor(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.pk}:{self.name}'
    
class movies_movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.TextField()

    def __str__(self):
        return f'{self.pk}:{self.title}'
    
class movie_actor_movies(models.Model):
    actor = models.ForeignKey(movie_actor,on_delete=models.CASCADE)
    movie = models.ForeignKey(movies_movie,on_delete=models.CASCADE)
    
class movies_review(models.Model):
    movie = models.ForeignKey(movies_movie,on_delete=models.CASCADE,related_name='review')
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.pk}:{self.title}'

    