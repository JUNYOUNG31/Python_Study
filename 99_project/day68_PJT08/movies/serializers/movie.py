from rest_framework import serializers
from ..models import movies_review, movie_actor, movies_movie
from movies.serializers.actor import ActorSerializer

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = movies_movie
        fields = '__all__'
    

class MovieSerializer(serializers.ModelSerializer):

    # class ActorSerializer(serializers.ModelSerializer):    
    #     class Meta:
    #         model = movie_actor
    #         fields = '__all__'
    
    # class ReivewSerializer(serializers.ModelSerializer):    
    #     class Meta:
    #         model = movies_review
    #         fields = '__all__'
    # title = serializers.CharField(min_length=2, max_length=100)
    # reviews = ReviewSerializer(many=True, read_only=True)    
    class Meta:
        model = movies_movie
        fields = '__all__'
    
    # actors = ActorSerializer(many=True, read_only=True)