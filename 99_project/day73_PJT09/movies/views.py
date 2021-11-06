from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_safe
from .models import Movie, Genre
from django.core.paginator import Paginator
from django.core import serializers
from django.http import HttpResponse
from datetime import date


# Create your views here.
@require_safe    
def index(request):
    genres = Genre.objects.all()
    movies = Movie.objects.order_by('-pk')        
    paginator = Paginator(movies,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.headers.get('x-requested-with') =='XMLHttpRequest':
        data = serializers.serialize('json', page_obj)
        return HttpResponse(data, content_type='application/json')
    context = {
        'genre_data':serializers.serialize('json', genres),
        'movies':page_obj,
    }    
    return render(request, 'movies/index.html', context)

@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)    
    context = {
        'movie':movie
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    startdate=date(2019,1,1)
    genres = Genre.objects.all()
    movielist = []
    for genre in genres:
        movie=Movie.objects.filter(release_date__range=(startdate, date.today())).filter(genres=genre.pk).order_by("vote_average")[:1]
        if movie and movie[0]not in movielist:
            movielist.append(movie[0])
    context = {
        'movies':movielist,
    }
    return render(request, 'movies/recommended.html', context)