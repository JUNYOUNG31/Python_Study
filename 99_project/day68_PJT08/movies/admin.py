from django.contrib import admin
from .models import movie_actor,movies_review,movies_movie

# Register your models here.

admin.site.register(movie_actor)
admin.site.register(movies_review)
admin.site.register(movies_movie)
