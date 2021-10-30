from rest_framework import serializers

from movies.serializers.movie import MovieSerializer
from ..models import movies_review, movie_actor, movies_movie


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = movies_review
        fields = ('title', 'content','rank',)
    

class ReviewSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(min_length=2, max_length=100)
    class Meta:
        model = movies_review
        fields = '__all__'
    movie = MovieSerializer(read_only=True)    
    