# day 61

## DB

## Model Relationship 1



## intro: 병원 진료 기록 시스템

###  1:N의 한계

```
* 의사 2명과 환자 2명 생성
* doctor1 - patient1
* doctor2 - patient2
* 한명의 환자가 2명의 의사에게 진료를 받고자함
* 하나의 외래 키에 2개의 의사 데이터를 넣을 수 없음

>> 새로운 객체를 생성해야한다
```

```python
# hospitals/models.py
from django.db import models

class Doctor(models.Model):
    name = models.TextField()
    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    name = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```



### 중개 모델(혹은 중개 테이블, Associative Table)작성

```
* doctor - reservation - patient
```

```python
# hospitals/models.py
from django.db import models

class Doctor(models.Model):
    name = models.TextField()
    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    name = models.TextField()    
    # 외래키 삭제
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
    
# 중개모델 작성
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```



###  ManyToManyField

```
* 다대다(M:N, many-to-many) 관계 설정 시 사용하는 모델 필드
* 하나의 필수 위치인자(M:N 관계로 설정할 모델 클래스)가 필요
* 필드 위치는 Doctor or Patient 모두 작성 가능
```

````python
# hospitals/models.py
from django.db import models

class Doctor(models.Model):
    name = models.TextField()
    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor)
    name = models.TextField()
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
````



### related_name

```
* target model(관계 필드를 가지지 않는 모델)이 source model(관계 필드를 가진 모델)을 참조할 때 사용할
  manager의 이름을 설정
* 즉, 역참조 시 사용하는 manager의 이름을 설정
* ForeignKey의 related_name과 동일
* 설정 후 기존의 _set 은 사용할 수 없다
```

```python
class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, related_name='patients')
```



## ManyToManyField

### 개념과 특징

```
* 다대다(M:N, many-to-many) 관계 설정 시 사용하는 모델 필드
* 하나의 필수 위치인자(M:N 관계로 설정할 모델 클래스)가 필요
* 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거 또는 만들 수 있다.
  * add(), remove()
```



### Arguments(인수)

```
1.related_name
* target model(관계 필드를 가지지 않는 모델)이 source model(관계 필드를 가진 모델)을 참조할 때 사용할
  manager의 이름을 설정
* ForeignKey의 related_name과 동일

2.through
* 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정
* 일반적으로 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우에 주로 사용

3.symmetrical
* ManyToManyField가 동일한 모델(on self)을 가리키는 정의에서만 사용
* symmetrical=True(기본값)일 경우 django는 person_set매니저를 추가하지 않음
* source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면, target 모델 인스턴스도 
  source 모델 인스턴스를 자동으로 참조하도록 함
* 즉, 인스타그램에서 내가 상대방을 팔로우 하면 상대방도 나를 자동으로 팔로우 한다
* 대칭을 원하지 않으면 False로 설정
```



### Related Manager

```
* 1:N 또는 M:N 관련 컨텍스트에서 사용되는 매니저
* 같은 이름의 메서드여도 각 관계(1:N,M:N)에 따라 다르게 사용 및 동작
  -1:N에서는 target 모델 인스턴스만 사용 가능
  -M:N에서는 관련된 두 객체에서 모두 사용 가능

* add()
  지정된 객체를 관련 객체 집합에 추가
  이미 존재하는 관계에 사용하면 관계가 복제되지 않음
  모델 인스턴스, pk 을 인자로 허용
  
* remove()
  관련 객체 집합에서 지정된 모델 객체를 제거
  내부적으로 QuerySet.delete()를 사용하여 관계가 삭제됨
  모델 인스턴스, pk 을 인자로 허용
```



### through

```python
class Doctor(models.Model):
    name = models.TextField()
    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
    

# 명령어   
reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')    
# 와 같이 뒤에 symptom을 통해서 해당 예약의 상태 증상을 추가로 작성할 수 있다.
```





## Like

### Like 구현하기

```python
# articles/models.py 에서 related_name='like_articles' 추가해줘야함(에러 발생 방지)
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    ...
# 에러 발생 원인
# like_users 필드 생성 시 자동으로 역참조는 .article_set 매니저를 생성
# 그러나 이전 1:N(User:Article) 관계에서 이미 해당 매니저이름을 사용중이기 때문에 중복 발생
# User와 관계된 ForeignKey 또는 ManytoManyField
```

```python
# articles/urls.py likes 추가
path('<int:article_pk>/likes/', views.likes , name='likes')

# articles/views.py
@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        # 좋아요 누름
        # 현재 좋아요를 요청하는 회원(request.user)이 해당 게시글의
        # 좋아요를 누른 회원 목록에 있다면,
        if article.like_users.filter(pk=request.user.pk).exists():
            # 좋아요 취소
            article.like_users.remove(request.user)
        else: # 좋아요 하기
            article.like_users.add(request.user)    
        return redirect('articles:index')
    return redirect('accounts:login')

# QuerySetAPI - exists()
# QuerySet에 결과가 포함되어 있으면 True를 반환하고 아니면 Flase 반환
# 특히 규모가 큰 QuerySet의 컨텍스트에서 특정 개체 존재 여부와 관련된 검색에 유용
# 고유한 필드(pk)가 있는 모델이 QuerySet의 구성원인지 여부를 찾는 가장 효율적인 방법
```

```django
<!--articles/index.html-->
...
<div>
  <form action="{% url 'articles:likes' article.pk %}" method="POST">
    {% csrf_token %}
    {% if user in article.like_users.all %}
      <input type="submit" value="좋아요 취소">
    {% else %}
      <input type="submit" value="좋아요">
    {% endif %}
  </form>
</div>
...
```



## Profile Page

### Profile page 작성

```
자연스러운 follow 흐름을 위한 회원 프로필 페이지 작성
```

```python
# accounts/url.py follow 추가
path('<username>/', views.profile, name='profile')

# accounts/views.py
def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context={
        'person':person,
    }
    return render(request, 'accounts/profile.html', context)
```

```django
<!--articles/index.html-->
{% extends 'base.html' %}
{% block content %}  
    <h1>{{ person.username }}의 프로필 페이지</h1>
	...
```

```django
<!--base.html 에 프로필 링크 추가--> 
{% if request.user.is_authenticated %}
      <h3>Hello, {{ user }}</h3>
      <a href="{% url 'accounts:profile' user.username %}">내 프로필</a>
...

<!--articles/index.html 에 프로필 링크 추가--> 
...
{% for article in articles %}
    <p>작성자 : 
      <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a>
...
```



## Follow

### Follow 구현

```python
# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers') 
```

```python
# accounts/url.py follow 추가
path('<int:user_pk>/follow/', views.follow, name='follow')

# accounts/views.py
@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        me = request.user
        you = get_object_or_404(get_user_model(),pk=user_pk)
        # person = get_object_or_404(get_user_model(),pk=user_pk)
        # 너와 내가 다른 사람이여야 팔로우를 진행할 수 있다.
        if me != you:
            # 내가 상대방(person)의 팔로워 목록에 있다면
            # if person.followers.filter(pk=request.user.pk).exists():
            if you.followers.filter(pk=request.user.pk).exists():
            #if request.user in person.followers.all():
                # 언팔로우
                you.followers.remove(me)
            else: # 팔로우
                you.followers.add(me)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
# 이해가 잘안되면 me you 로 해석하면 쉽게 해석 가능
```

```django
<!-- profile 페이지에서 팔로우와 언팔로우 버튼 작성 -->

{% with  followings=person.followings.all followers=person.followers.all  %}
    <h1>{{ person.username }}의 프로필 페이지</h1>
      <div>
        <div>팔로잉 수 : {{ followings|length }}/ 팔로워 수 : {{ followers|length }}</div>
      </div>
      {% if user != person %}
        <div>
          <form action="{% url 'accounts:follow' person.pk %}" method="POST">
            {% csrf_token %}qq
            {% if user in followers %}
              <input type="submit" value="언팔로우">
            {% else %}
              <input type="submit" value="팔로우">
            {% endif %}
          </form>
        </div>
      {% endif %}
    {% endwith %}
<!--with 를 사용해서 구간을 정하고 변수 처리를 사용할 수 있다-->
```





