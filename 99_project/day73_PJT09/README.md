# pjt 09

## 📜소감



```
이전에 배운 자바스크립트의 좋아요와 팔로우를 다시공부하면서 진행하였고 인피니트 스크롤을 하면서 많은부분에서 막혔다.
일단 구현 까지는 완료했는데 그다음에 부트스트랩으로 전체적으로 꾸미면서 카드로 표현하여 2개씩 5줄 나오고 그다음에 인피니트 스크롤을 구현할려고 했는데 잘안되었다. 그후에 원상복구 후에 인피니트 스크롤을 진행하려고 하는데 작동이 안되는 에러가 발생하여 애를 먹었다.
아직까지 많이 부족해서 공부가 많이 필요하다....프론트가 재미있는 한데 어렵기도 해서 어지럽다
```

```txt
 view에서 데이터를 가공하고 html에서 사용하는데 머릿 속에서 생각한 대로 휙휙 그리기에는 연습이 많이 부족했던 것 같다. 앞의 실습 파일들을 참고하면서 완성할 수 있었고 특히 어떤 기능을 새로 완성하는 데 있어서 공식 문서를 원활히 사용하고 검색을 잘 활용하는 게 앞으로 관건인 것 같다. 추천 영화를 완성하는 데 있어서 view 에서 함수를 구성할 때 쿼리에 대한 애매한 지식으로 더 헤맸던 것 같다. 공식 문서를 더더욱 신봉해야겠다.
```



## ⚙구현과정

#### 서술

```
구현과정
(1) 자바스크립트와 axios를 사용해서 유저 팔로우를 구현
(2) 위와 마찬가지로 좋아요 버튼 구현
(3) 영화 데이터를 loaddata 를 사용해서 데이터를 받기
    1) movies/index.html 작성 - views.py 작성후에 작성
       인피니트 스크롤 추가
    2) movies/detail.html 작성 - views.py 작성 후에 작성
       필요한 데이터 추가

(4)

학습내용
javascript와 axios를 사용해서 전체적인 프로젝트를 만드는 과정이였고 복습 개념도 있었으며 오늘 유튜브에서 알려주신 내용으로 적용해 보았다.
```

#### movies/views.py

```python
# movies/views.py

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
```



#### movies/index.html

```html
<!-- movies/index.html -->

{% extends 'base.html' %}
{% block content %}

<h1 class="d-flex justify-content-center">Movies</h1>
  <div class='movielist'>
    <div class="row row-cols-2">
      {% for movie in movies %}
      <div id="movie"> 
      <div class="col">   
        <div class="card">
          <img src="{{movie.poster_path}}" class="card-img-top" alt="{{movie.title}}" width="150">
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
            <hr>
            {% for genre in movie.genres.all %} 
            <span class="card-title">{{ genre.name }}</span>
            {% endfor %}
            <hr>
            <p class="card-text" style="overflow:hidden;white-space:nowrap;text-overflow:ellipsis;">{{ movie.overview }}</p>
            <a href="{% url 'movies:detail' movie.pk %}">[DETAIL]</a>
          </div>
        </div>
        </div>
      </div>
    {% endfor %}
    </div>
  </div>

<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
  let pageNum = 2
  document.addEventListener('scroll', (event) => {
    // console.log(event)
    const { scrollHeight, scrollTop, clientHeight } = document.documentElement
    // console.log(scrollHeight, scrollTop, clientHeight)    
    if (scrollHeight - Math.round(scrollTop) === clientHeight) {
      axios({
      method: 'get',
      url: `/movies/?page=${pageNum}`,
      headers: {'x-requested-with': 'XMLHttpRequest'}
    })
      .then((response) => {
        const movies = response.data       
        // console.log(movies)
        movies.forEach((movie) => {
            const movieList = document.querySelector('.row-cols-2')
            const movieDiv = document.createElement('div')
        // console.log(movie)        
        const m = "{{ genre_data|escapejs }}"        
        const genre_pk = JSON.parse(m)
        const genrenames = movie.fields.genres.reduce((pre,el) => {      
          const gname = genre_pk.filter(e=>e.pk==el)[0].fields.name
          return pre + `<span class="card-title">${ gname } </span>`
        },'')        
        // console.log(movie)
        const movieHTML = 
         `
          <div class="col">   
            <div class="card">
              <img src="${movie.fields.poster_path}" class="card-img-top" alt="${movie.fields.title}" width="150">
              <div class="card-body">
                <h5 class="card-title">${ movie.fields.title }</h5>
                <hr>                
                ${genrenames}
                <hr>
                <p class="card-text" style="overflow:hidden;white-space:nowrap;text-overflow:ellipsis;">${ movie.fields.overview }</p>
                <a href="${movie.pk}/">[DETAIL]</a>
              </div>
            </div>
          </div>
          `
          // console.log(movieHTML)
          movieDiv.innerHTML = movieHTML
          // console.log(movieDiv)
          movieList.appendChild(movieDiv)
          // console.log(movieHTML)
        })    
        pageNum += 1
      })
    }
    // console.log(clientHeight)
    // console.log(scrollHeight - Math.round(scrollTop))
    // console.log('----------------------------------')
  })    
</script>

{% endblock %}
```



#### movies/detail.html

```django
<!-- movies/detail.html -->

{% extends 'base.html' %}

{% block content %}
<h1>[DETAIL]</h1>
<hr>
  <p>Title: {{ movie.title }}</p>
  <hr>
  <img src="{{ movie.poster_path }}" alt="movie.title">  
  <p>Release: {{ movie.release_date }}</p>
  <hr>
  <p>Genres:
    {% for genre in movie.genres.all %}
      <span class="card-title">{{ genre.name }}</span>
    {% endfor %}
  </p>
  
  <hr>
  <p>Popular: {{ movie.popularity }}</p>
  <hr>
  <p>All_vote : {{ movie.vote_count }}</p>
  <hr>
  <p>Age_vote: {{ movie.vote_average }}</p>
  <hr>
  <p>Overview</p>
  <p>{{ movie.overview }}</p>  
  <hr>
<a href="{% url 'movies:index' %}">[BACK]</a>
{% endblock %}
```

```txt
자바스크립트를 하며 id와 class를 스크립트에서 적절히 사용해서 다른 event나 method를 통해 활용하는 법을 주로 익힌 것 같다. 이전에는 하나의 list나 dictionary 안에 있는 것이 명시적으로 모두 보였고 직접 만들어서 사용했다면 axios를 사용하고 html로 데이터를 받아오면서 우리가 구성하지 않은 데이터에 대한 접근이 정말 어려웠다. console 창에서 일일이 log를 찍어가며 깨달았다. div 나 input으로 받은 데이터를 script에서 사용하기 위해 불러오는 법 많은 event들과 공식 문서 없이는 프로젝트를 해내기가 어려웠다.

profile - follow구현
button click으로 이벤트가 발생
follow switch 
변경된 button innertext과 follower 수를 보여주었다.

추천 영화
2019년 1월 1일 이후부터 오늘까지 개봉된 영화 중에서 평점이 높은 영화를 filter로 구해서 QuerySet의 0번째 객체를 도출
객체가 값이 있고 movielist에 없으면 넣어서 html로 보낸다.

중복이 없고 장르에서 평점이 가장 높은 영화를 하나씩 보여준다.
```



#### accounts/profiles-script

```html
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const forms = document.querySelectorAll('.followform')
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    forms.forEach(form => {
      form.addEventListener('submit', function(event) {
        event.preventDefault()
        const profileId = event.target.dataset.profileId
        axios({
          method:'post',
          url: `http://127.0.0.1:8000/accounts/${profileId}/follow/`,
          headers: {
            'X-CSRFToken': csrftoken
          }
        })
        .then(response => {
          const follow = response.data.follow
          const followCount = response.data.followCount
          const followBtn = document.querySelector(`#follow-${profileId}`)
          const followCountNum = document.querySelector(`#follow-count-${profileId}`)
          followBtn.innerText = follow ? '언팔로우' : '팔로우'
          followBtn.style.color = follow ? 'red' : 'blue'
          followCountNum.innerText = followCount

        })
      })
    })
  </script>
```



#### accounts/views-follow

```python
@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        user = request.user
        if person != user:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                follow = False
            else:
                follow = True
                person.followers.add(user)
            context = {
                'follow':follow,
                'followCount':person.followers.count(),
                'person.username':person.username,
            }
        return JsonResponse(context)
    return redirect('accounts:login')
```

#### movies/views-recommended

```python
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
```

