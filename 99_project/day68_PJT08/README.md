후기

```txt
구현 과정 & 학습 내용

영화배우, 영화, 리뷰를 각각 모델로 만들고 중개테이블로 영화배우와 영화의 관계를 구축하려고 시도했다. restful한 url을 모델과 모델pk로 수직적인 관계로 의도를 보기 쉽게 만들었다. get put post delete method를 사용해서 각각에 맞는 읽기, 생성, 수정, 삭제를 하는데 완료했으며 serializer를 사용했다.

DB에 서로 다른 모델이 서로를 참조해서 서로의 데이터를 가져오게 만드는 법과 그 구조들 그리고 직렬화를 사용해서 요청을 보냈을 때 json형식으로 다루기 쉬운 형태로 정보를 받아서 처리하는 방법에 대해서 중점적으로 실습했다.

```

```txt
어려웠던 점 & 느낀 점

모델 간의 관계를 view에서 사용하는 것과 테이블을 구상하는 게 힘들었다. 여러가지 방법이 있었고 그 중에서 가장 효율적이고 간결한 방법을 찾고 싶었는데 많은 연습을 거쳐야 할 것 같다.

DB에서 모델을 구성한다는 게 모든 것의 시작이라고 생각해서 쉬울 줄 알았는데 마지막까지 모델이 사용된다는 점을 고려했을 때 가장 많은 시간과 노력이 들어가야하는 부분인 것 같다. 참조와 역참조에 대한 내용 ManyToManyField 와 외래키를 사용할 수 있는데 어떤 부분에서 뭘 사용해야 좋을지 아직 확실히 모르겠다. 관련된 실습코드를 많이 뜯어봐야겠다.
```



```
이번 프로젝트는 DB를 기반으로 REST API를 설계하는 프로젝트이다. DRF와 Serializer를 이용해서 설계하는 과정이였는데, 생각보다 구현과정에 있어서 힘들었던점이 많았다. 계속해서 교재와 강사님의 코드를 비교해가면서 오류를 찾았고 코드의 흐름을 파악하는데 집중했음. 어려웠던점은 모델과 테이블간의 참조와 역참조를 활용해서 데이터를 가져오는 부분이 제일 힘들었던것 같다. 선택사항도 하고 싶었는데 시간이 부족해서 해결하지 못했다.
공부가 필요하다...
```

```
구현과정
model 과 serializer를 구성하면서 변경해야 할 부분들이 많이 발생해서 data를 계속해서 만들고 지워가면서 반복해서 구현하였다.
url의 경로를 필요한 정보에 맞춰서 작성하였다.
학습내용
DRF와 serializer의 활용과 ERD에 따라 Model에 설정하고 REST API를 설계하고 URL을 어떻게 잘 만들 수 있는지 학습
```

```python


# models.py
from django.db import models

class movie_actor(models.Model):
    name = models.CharField(max_length=100)    
    def __str__(self):
        return f'{self.pk}:{self.name}'    
class movies_movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.TextField()
    def __str__(self):
        return f'{self.pk}:{self.title}'    
class movie_actor_movies(models.Model):
    actor = models.ForeignKey(movie_actor,on_delete=models.CASCADE)
    movie = models.ForeignKey(movies_movie,on_delete=models.CASCADE)    
class movies_review(models.Model):
    movie = models.ForeignKey(movies_movie,on_delete=models.CASCADE,related_name='review')
    title = models.CharField(max_length=100)
    content = models.TextField()
    rank = models.PositiveIntegerField()
    def __str__(self):
        return f'{self.pk}:{self.title}'   
```

```python
# serializers
from rest_framework import serializers
from ..models import movies_review, movie_actor, movies_movie
from movies.serializers.actor import ActorSerializer
from movies.serializers.movie import MovieSerializer

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie_actor
        fields = '__all__'  
class ActorSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(min_length=2, max_length=100)
    class Meta:
        model = movie_actor
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = movies_movie
        fields = '__all__'   
class MovieSerializer(serializers.ModelSerializer): 
    class Meta:
        model = movies_movie
        fields = '__all__'
        
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = movies_review
        fields = ('title', 'content','rank',)    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = movies_review
        fields = '__all__'
    movie = MovieSerializer(read_only=True)                
```

```python
# urls.py

from django.urls import path
from . import views
urlpatterns = [
    path('actors/',views.actor_list),
    path('actors/<int:actor_pk>/',views.actor_detail),
    path('movies/',views.movie_list_or_create),
    path('movies/<int:movie_pk>/',views.movie_detail),
    path('movies/<int:movie_pk>/reviews/',views.review_list_or_create),
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/',views.review_detail_or_update_or_delete),    
    # path('movies/<int:movie_pk>/actors/<int:actor_pk>',views.actor_enroll),
]
```

