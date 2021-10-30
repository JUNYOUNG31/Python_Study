from rest_framework import serializers
from ..models import movies_review, movie_actor, movies_movie


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie_actor
        fields = '__all__'
    

class ActorSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(min_length=2, max_length=100)
    class Meta:
        model = movie_actor
        fields = '__all__'