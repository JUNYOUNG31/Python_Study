# pjt 09

## ๐์๊ฐ



```
์ด์ ์ ๋ฐฐ์ด ์๋ฐ์คํฌ๋ฆฝํธ์ ์ข์์์ ํ๋ก์ฐ๋ฅผ ๋ค์๊ณต๋ถํ๋ฉด์ ์งํํ์๊ณ  ์ธํผ๋ํธ ์คํฌ๋กค์ ํ๋ฉด์ ๋ง์๋ถ๋ถ์์ ๋งํ๋ค.
์ผ๋จ ๊ตฌํ ๊น์ง๋ ์๋ฃํ๋๋ฐ ๊ทธ๋ค์์ ๋ถํธ์คํธ๋ฉ์ผ๋ก ์ ์ฒด์ ์ผ๋ก ๊พธ๋ฏธ๋ฉด์ ์นด๋๋ก ํํํ์ฌ 2๊ฐ์ฉ 5์ค ๋์ค๊ณ  ๊ทธ๋ค์์ ์ธํผ๋ํธ ์คํฌ๋กค์ ๊ตฌํํ ๋ ค๊ณ  ํ๋๋ฐ ์์๋์๋ค. ๊ทธํ์ ์์๋ณต๊ตฌ ํ์ ์ธํผ๋ํธ ์คํฌ๋กค์ ์งํํ๋ ค๊ณ  ํ๋๋ฐ ์๋์ด ์๋๋ ์๋ฌ๊ฐ ๋ฐ์ํ์ฌ ์ ๋ฅผ ๋จน์๋ค.
์์ง๊น์ง ๋ง์ด ๋ถ์กฑํด์ ๊ณต๋ถ๊ฐ ๋ง์ด ํ์ํ๋ค....ํ๋ก ํธ๊ฐ ์ฌ๋ฏธ์๋ ํ๋ฐ ์ด๋ ต๊ธฐ๋ ํด์ ์ด์ง๋ฝ๋ค
```

```txt
 view์์ ๋ฐ์ดํฐ๋ฅผ ๊ฐ๊ณตํ๊ณ  html์์ ์ฌ์ฉํ๋๋ฐ ๋จธ๋ฆฟ ์์์ ์๊ฐํ ๋๋ก ํํ ๊ทธ๋ฆฌ๊ธฐ์๋ ์ฐ์ต์ด ๋ง์ด ๋ถ์กฑํ๋ ๊ฒ ๊ฐ๋ค. ์์ ์ค์ต ํ์ผ๋ค์ ์ฐธ๊ณ ํ๋ฉด์ ์์ฑํ  ์ ์์๊ณ  ํนํ ์ด๋ค ๊ธฐ๋ฅ์ ์๋ก ์์ฑํ๋ ๋ฐ ์์ด์ ๊ณต์ ๋ฌธ์๋ฅผ ์ํํ ์ฌ์ฉํ๊ณ  ๊ฒ์์ ์ ํ์ฉํ๋ ๊ฒ ์์ผ๋ก ๊ด๊ฑด์ธ ๊ฒ ๊ฐ๋ค. ์ถ์ฒ ์ํ๋ฅผ ์์ฑํ๋ ๋ฐ ์์ด์ view ์์ ํจ์๋ฅผ ๊ตฌ์ฑํ  ๋ ์ฟผ๋ฆฌ์ ๋ํ ์ ๋งคํ ์ง์์ผ๋ก ๋ ํค๋งธ๋ ๊ฒ ๊ฐ๋ค. ๊ณต์ ๋ฌธ์๋ฅผ ๋๋์ฑ ์ ๋ดํด์ผ๊ฒ ๋ค.
```



## โ๊ตฌํ๊ณผ์ 

#### ์์ 

```
๊ตฌํ๊ณผ์ 
(1) ์๋ฐ์คํฌ๋ฆฝํธ์ axios๋ฅผ ์ฌ์ฉํด์ ์ ์  ํ๋ก์ฐ๋ฅผ ๊ตฌํ
(2) ์์ ๋ง์ฐฌ๊ฐ์ง๋ก ์ข์์ ๋ฒํผ ๊ตฌํ
(3) ์ํ ๋ฐ์ดํฐ๋ฅผ loaddata ๋ฅผ ์ฌ์ฉํด์ ๋ฐ์ดํฐ๋ฅผ ๋ฐ๊ธฐ
    1) movies/index.html ์์ฑ - views.py ์์ฑํ์ ์์ฑ
       ์ธํผ๋ํธ ์คํฌ๋กค ์ถ๊ฐ
    2) movies/detail.html ์์ฑ - views.py ์์ฑ ํ์ ์์ฑ
       ํ์ํ ๋ฐ์ดํฐ ์ถ๊ฐ

(4)

ํ์ต๋ด์ฉ
javascript์ axios๋ฅผ ์ฌ์ฉํด์ ์ ์ฒด์ ์ธ ํ๋ก์ ํธ๋ฅผ ๋ง๋๋ ๊ณผ์ ์ด์๊ณ  ๋ณต์ต ๊ฐ๋๋ ์์์ผ๋ฉฐ ์ค๋ ์ ํ๋ธ์์ ์๋ ค์ฃผ์  ๋ด์ฉ์ผ๋ก ์ ์ฉํด ๋ณด์๋ค.
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
์๋ฐ์คํฌ๋ฆฝํธ๋ฅผ ํ๋ฉฐ id์ class๋ฅผ ์คํฌ๋ฆฝํธ์์ ์ ์ ํ ์ฌ์ฉํด์ ๋ค๋ฅธ event๋ method๋ฅผ ํตํด ํ์ฉํ๋ ๋ฒ์ ์ฃผ๋ก ์ตํ ๊ฒ ๊ฐ๋ค. ์ด์ ์๋ ํ๋์ list๋ dictionary ์์ ์๋ ๊ฒ์ด ๋ช์์ ์ผ๋ก ๋ชจ๋ ๋ณด์๊ณ  ์ง์  ๋ง๋ค์ด์ ์ฌ์ฉํ๋ค๋ฉด axios๋ฅผ ์ฌ์ฉํ๊ณ  html๋ก ๋ฐ์ดํฐ๋ฅผ ๋ฐ์์ค๋ฉด์ ์ฐ๋ฆฌ๊ฐ ๊ตฌ์ฑํ์ง ์์ ๋ฐ์ดํฐ์ ๋ํ ์ ๊ทผ์ด ์ ๋ง ์ด๋ ค์ ๋ค. console ์ฐฝ์์ ์ผ์ผ์ด log๋ฅผ ์ฐ์ด๊ฐ๋ฉฐ ๊นจ๋ฌ์๋ค. div ๋ input์ผ๋ก ๋ฐ์ ๋ฐ์ดํฐ๋ฅผ script์์ ์ฌ์ฉํ๊ธฐ ์ํด ๋ถ๋ฌ์ค๋ ๋ฒ ๋ง์ event๋ค๊ณผ ๊ณต์ ๋ฌธ์ ์์ด๋ ํ๋ก์ ํธ๋ฅผ ํด๋ด๊ธฐ๊ฐ ์ด๋ ค์ ๋ค.

profile - follow๊ตฌํ
button click์ผ๋ก ์ด๋ฒคํธ๊ฐ ๋ฐ์
follow switch 
๋ณ๊ฒฝ๋ button innertext๊ณผ follower ์๋ฅผ ๋ณด์ฌ์ฃผ์๋ค.

์ถ์ฒ ์ํ
2019๋ 1์ 1์ผ ์ดํ๋ถํฐ ์ค๋๊น์ง ๊ฐ๋ด๋ ์ํ ์ค์์ ํ์ ์ด ๋์ ์ํ๋ฅผ filter๋ก ๊ตฌํด์ QuerySet์ 0๋ฒ์งธ ๊ฐ์ฒด๋ฅผ ๋์ถ
๊ฐ์ฒด๊ฐ ๊ฐ์ด ์๊ณ  movielist์ ์์ผ๋ฉด ๋ฃ์ด์ html๋ก ๋ณด๋ธ๋ค.

์ค๋ณต์ด ์๊ณ  ์ฅ๋ฅด์์ ํ์ ์ด ๊ฐ์ฅ ๋์ ์ํ๋ฅผ ํ๋์ฉ ๋ณด์ฌ์ค๋ค.
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
          followBtn.innerText = follow ? '์ธํ๋ก์ฐ' : 'ํ๋ก์ฐ'
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

