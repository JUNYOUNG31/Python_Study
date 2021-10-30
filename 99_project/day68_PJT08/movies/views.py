from django.db.models import manager
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from .models import movie_actor, movies_movie, movies_review
from .serializers.actor import ActorListSerializer, ActorSerializer
from .serializers.movie import MovieListSerializer, MovieSerializer
from .serializers.review import ReviewListSerializer, ReviewSerializer
from rest_framework.response import Response



# Create your views here.
@api_view(['GET'])
def actor_list(request):
    actors = movie_actor.objects.all()
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(movie_actor, pk=actor_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)

@api_view(['GET', 'POST']) 
def movie_list_or_create(request):
    if request.method=='GET':
        movies = movies_movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method=='POST':       
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    

@api_view(['GET']) 
def movie_detail(request,movie_pk):    
    movie = get_object_or_404(movies_movie, pk=movie_pk)    
    serializer = MovieSerializer(movie)
    return Response(serializer.data)   


@api_view(['GET','POST'])
def review_list_or_create(request, movie_pk):
    if request.method=='GET':
        reviews = movies_review.objects.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        movie = get_object_or_404(movies_movie, pk=movie_pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data)

    
@api_view(['GET','PUT','DELETE'])
def review_detail_or_update_or_delete(request,review_pk, movie_pk):
    review = get_object_or_404(movies_review, pk=review_pk)
    movie = get_object_or_404(movies_movie, pk=movie_pk)
    if request.method=='GET':
        serializer = ReviewSerializer(review)        
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET','POST'])
# def actor_enroll(request, movie_pk, actor_pk):
#     movie = get_object_or_404(movies_movie, pk=movie_pk)    
#     actor = get_object_or_404(movie_actor, pk=actor_pk)
#     serializer = MovieSerializer(instance=movie, data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(actor=actor)
#         return Response(serializer.data)