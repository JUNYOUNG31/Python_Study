from django.shortcuts import redirect, render
from .models import Movie
# Create
## 사용자가 데이터를 제출할 빈 html을 제공
def new(request):
    return render(request, 'movies/new.html')

## 사용자가 제출한 데이터를 새로운 movie에 저장
def create(request):
    title = request.POST.get('title')
    overview = request.POST.get('overview')
    poster_path = request.POST.get('poster_path')
    movie = Movie(title=title, overview=overview, poster_path=poster_path)    
    movie.save()
    return redirect('movies:detail', movie.pk)
        

# Read
## 전체 질문 목록 조회
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)


## 단일 질문 상세 조회
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie':movie,
    }
    return render(request, 'movies/detail.html', context)


# Update
## 데이터를 제풀할 기존 내용이 있는 html 제공
def edit(request, pk):
    movie = Movie.objects.get(pk=pk)  
    context = {
        'movie': movie,
    }
    return render(request, 'movies/edit.html', context)


## 사용자가 제출한 데이터를 기존 movie에 저장
def update(request, pk):
    movie = Movie.objects.get(pk=pk)    
    movie.title = request.POST.get('title')
    movie.overview = request.POST.get('overview')
    movie.poster_path = request.POST.get('poster_path')
    movie.save()
    return redirect('movies:detail', movie.pk)

# Delete
## 기존 movie을 삭제
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)  
    if request.method == "POST":        
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie.pk)