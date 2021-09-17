# PROJECT 05

## 후기

``` 
박** 후기:  오,,,, 장고 응용이 아니라 복습하는 내용이라 매우 다행이다.
프로젝트 구현을 끝내고 index 페이지에 사진을 넣고 싶었는데 몇번의 시도 끝에 성공
데이터가 유효하지 않을 때 에러메시지를 포함하라고 되어 있었다.
데이터가 분명 유효하지 않았는데 에러메시지가 뜨지 않는다,,?
안 뜨는 줄 알았더니 스페이스 바 하나 톡 누르고 제출하니 뜬다.
스무스한 관통 프로젝트였다✨
처음으로 한 협업 프로젝트였고 까다로운 과제가 아니였기 때문에 스무스했다 ✨
```

```
박** 후기: 이번 프로젝트는 지금까지 배웠던 내용을 복습하는 과정이 였는데 
두명이서 pair로 진행하는 방식으로 했기때문에 이전의 프로젝트와는 조금 다른 느낌이였다.
구현하는 과정은 계속하던거라서 따라는 쓰는데 완전하게 이해되지 않는다.
이미지를 추가할려고 시도를 했는데 잘안되다가 추가하는데 성공함
에러 메세지를 작성하는 부분에서 구현이 된것인지 아닌지 확실하지 않아서 강사님께 질문도 했지만
구현해놓고 사용방법을 몰라서 시간을 날렸다. 정확하게 개념을 이해하고 사용할 수 있게 복습하겠다.......
```



## A. 프로젝트 구조

우선 시작하기 전

> 1. 가상환경 생성 및 활성화
> 2. 필요한 패키지 다운로드 하기(django)
> 3. requirements.txt에 pip list 저장해놓기



폴더 및 앱 만들기

```python
django-admin startproject pjt05 .
python manage.py startapp movies
```

필요한 파일 생성하기

```python
touch .gitignore README.md README-박신영.md README-박준영.md
```



## B. Model

필요한 field는 총 3개 이며 Movie 클래스에 추가해준다.

```python
from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)


    def __str__(self):
        return self.title
```



## C. Form

models에서 생성한 Movie를 상속받을 것이며 각 field에 필요한 정보를 MovieForm에 작성

```python
from django import forms 
from .models import Movie

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        max_length= 100,
        error_messages={
            'required': '내용을 입력해주세요'
        },
    )
    
    overview = forms.CharField(
        label='줄거리',
        widget=forms.Textarea(),
        
        error_messages={
            'required': '내용을 입력해주세요'
        },
    )

    poster_path = forms.CharField(
        label='포스터 경로',
        max_length=500,
        error_messages={
            'required': '내용을 입력해주세요'
        },
    )

    
	# Movie를 상속 받을 것!
    class Meta:
        model = Movie
        fields = '__all__'
```



## D. Admin

```python
관리자 페이지에서 Movie 모델의 데이터 생성, 조회, 수정, 삭제가 가능합니다.

#admin.py	
from .models import Movie  # 추가
admin.site.register(Movie) # 추가

$ python manage.py createsuperuser # 명령어를 통해서 관리자 계정을 만든다.


django에서 제공하는 admin 이기때문에 작성하는데 큰어려움은 없음
```



## E. URL

```python
HTTP verb   URL                       패턴 설명
GET & POST  /movies/create/ Form      표시 및 영화 데이터 생성
GET 		/movies/ 			      전체 영화 목록 조회
GET 		/movies/<pk>/ 		      단일 영화 상세 조회
GET & POST  /movies/<pk>/update/ Form 표시 및 영화 데이터 수정
POST 		/movies/<pk>/delete/      단일 영화 삭제


프로젝트의 urls.py 에 생성한 app의  urls을 추가한다.
#pjt05/urls.py
from django.contrib import admin
from django.urls import path, include # 추가
urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),  # 추가
]

app의 urls에 사용할 URL 패턴을 설정
#movies.
from django.urls import path
from .import views
app_name = 'movies'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),        # pk가 필요한 부분은 추가
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),  
]

이부분은 계속해서 반복하는 부분이라서 크게 어려움은 없음.
```



## F. View & Template

```django
i. 공유 템플릿 생성 및 사용
    1. 모든 HTML파일은 base.html을 확장(extends)하여 사용합니다.
    2. base.html은 모든 페이지가 공유하는 상단 네비게이션 바를 표시합니다.
    3. 네비게이션 바는 전체 영화 목록 조회 페이지와 새로운 영화 작성 페이
	   지로 이동할 수 있는 링크를 포함합니다.	   
	   
#templates/base.html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div >
        <a class="navbar-brand ms-4" href="{% url 'movies:index' %}">INDEX</a>
        <a href="{% url 'movies:create' %}" class='navbar-brand'>CREATE</a>
    </div>
</nav>
<div class="container">
    {% block content %}  
    {% endblock %}
</div>
nav 바를 추가했고 a 태그를 사용해서 index 와 create 페이지를 구현
block 부분을 container로 감싸줘서 벽에서 조금 떨어지게 구성

조금 썰렁한거 같아서 이미지를 추가할려고했는데 잘안됨
```

```python
ii. 전체 영화 목록 조회
    1. 데이터베이스에 존재하는 모든 영화의 목록을 표시합니다.
    2. 사용자에게 응답으로 제공할 HTML파일은 index.html 입니다.
    3. index.html은 base.html을 확장합니다.
    4. index.html에는 적절한 HTML요소를 사용하여 제목을 표시하며, 제목을
       클릭 시 해당 영화의 상세 조회 페이지로 이동합니다.

index.html을 나타내기 위해서 정보를 가져오기
# views.py
...
@require_safe
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {'movies':movies,}
    return render(request, 'movies/index.html', context)
...

# index.html 
{% extends 'base.html' %}
{% load static %}
{% block content %}
  <img src="{% static 'images/logo.jpg' %}" alt="logo image">
  <hr>
  {% for movie in movies %}
    <a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a>
    <p>글 번호: {{ movie.pk }}</p>
    <p>줄거리: {{ movie.overview }}</p>
    <p>포스터 경로: {{ movie.poster_path }}</p>
    <hr>
  {% endfor %}
{% endblock content %}

base.html 을 extends로 불러와서 최상단에 위치시킨다.
로고 이미지도 추가했다.
그후 for 문을 통해서 목록을 가져오는데 title로 가져오고 a 태그를 사용해서 detail 페이지로 링크 설정
글 번호, 줄거리, 포스터 경로 가 모두 표시되도록 설정하였다.
```

```django
iii. 새로운 영화 작성 (GET)
    1. 사용자에게 응답으로 제공할 HTML파일은 create.html 혹은 form.html입니다.
    2. create.html 혹은 form.html은 base.html을 확장합니다.
    3. 영화를 작성할 수 있는 Form을 표시하며, ModelForm을 이용하여 다음과 같은 
    input 요소들을 포함해야 합니다.
    4. Form에 작성한 정보는 제출(submit)시, 
    사용자 제출 데이터를 저장하는 URL로 요청과 함께 전송됩니다.   

# create.html
{% extends 'base.html' %}
{% block content %}
  <h1>CREATE</h1>
  <form action="{% url 'movies:create' %}" method='POST'>
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="제출" class='btn btn-warning'>
  </form>
{% endblock content %}

생성한 form.py의 데이터를 가져와서 작성하게 만들었음
```

```python
iv. 새로운 영화 작성 (POST)
    1. ModelForm을 이용하여 요청과 함께 전송된 데이터를 검증합니다.
    2. 데이터가 유효하다면 데이터베이스에 저장하고 상세 조회 페이지로 redirect합니다.
    3. 데이터가 유효하지 않다면 에러 메시지를 포함하여 데이터를 작성하는 Form을 다시 표시합니다.
    
    
# views.py
...
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {'form': form,}
    return render(request, 'movies/create.html', context)
...

데이터를 불러오고 저장하고 나타내는 과정이 어렵긴하다.
반복적으로 하고 있기는한데 정확하게 이해하는데는 좀 걸릴것 같다.

# forms.py
...
class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        max_length= 100,
        error_messages={
            'required': '내용을 작성해주세요!'
        },
    )
...

forms.py 에서 에러메세지를 표시하게 설정한다.
이부분이 처음에 구현이 안되는줄 알았는데 공백만 넣었을때 작용하는 에러라는 것을 알게 되었다.
```

```python
v. 단일 영화 상세 조회
    1. 영화의 상세정보를 HTML에 표시합니다.
    2. 표시할 영화의 pk는 URL과 함께 전달된 영화의 id입니다.
    3. 사용자에게 응답으로 제공할 HTML은 detail.html입니다.
    4. detail.html은 base.html을 확장합니다.
    5. detail.html에는 적절한 HTML 요소를 사용하여, 조회하는 영화의 제목, 
       줄거리, 포스터 이미지를 표시합니다

# views.py
...
@require_safe
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {'movie':movie,}
    return render(request, 'movies/detail.html', context)
...

# detail.html
{% extends 'base.html' %}
{% block content %}
  <h1>DETAIL</h1>
  <hr>
  <h3>제목: {{ movie.title }}</h3>
  <p>줄거리: {{ movie.overview }}</p>
  <p>포스터 경로: {{ movie.poster_path }}</p>
  <a href="{% url 'movies:update' movie.pk %}">
    <button class='btn btn-primary'>EDIT</button>
  </a>
  <form action="{% url 'movies:delete' movie.pk %}" method='POST'>
    {% csrf_token %}
    <button class='btn btn-danger'>DELETE</button>
  </form>
{% endblock content %}

이부분은 생성한 정보들을 pk를 통해서 가져오는 것이기 때문에 그렇게 어렵지는 않은 부분이다.
원하는 정보와 수정과 삭제 기능을 추가했다.
```

```python
vi. 영화 데이터 수정 (GET)
1. 사용에게 제공 할 update.html 파일 생성
2. 사용자가 제출한 응답은 POST 방식으로 해당 pk의 update url로 전송될 것.

{% extends 'base.html' %}

{% block content %}
  <h1>UPDATE</h1>
  <form action="{% url 'movies:update' movie.pk %}" method='POST'>
    {% csrf_token %}
    {{ form.as_p }}

    <button class='btn btn-success'>수정</button>
  </form>
{% endblock content %}
```

```python
vii. 영화 데이터 수정 (POST)

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    # 업데이트 할 객체를 선택
    movie = Movie.objects.get(pk=pk)
    # 이 객체의 전송 방식이 POST이고 
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie, files=request.FILES)
        # 해당 객체의 데이터가 유효하다면 db에 저장하고 해당 객체의 상세 조회 페이지로 넘어 감. 
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)

    else:
        # 데이터가 유효하지 않다면 에러 메시지와 수정할 내용이 있는 form이 표시될 것
        form = MovieForm(instance=movie)
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/update.html', context)
```

```python
viii. 영화 데이터 삭제

@require_http_methods
def delete(request, pk):
    # 삭제할 객체를 선택
    movie = Movie.objects.get(pk=pk)
    # 만약 데이터 전송 방식이 POST라면 삭제 후 인덱스 페이지로 redirect
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        # 데이터의 전송 방식이 POST가 아니라면 삭제하지 않고 해당 pk의 detail 페이지로 redirect
        return redirect('movies:detail', movie.pk)
```

