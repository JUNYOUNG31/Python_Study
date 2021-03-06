# day 59

## DB

## Model Relationship 1



## Foreign Key

### 외래 키

```
* 관계형 데이터베이스에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키
* 참조하는 테이블에서 1개의 키에 해당하고, 참조되는 테이블의 기본 키를 가리킨다
* 참조하는 테이블의 행 1개의 값은, 참조되는 테이블의 행 값에 대응
```



### 특징

```
* 참조 무결성
데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성
외래 키가 선언된 테이블의 외래키 속성 값은 그 테이블의 부모가 되는 테이블의 기본 키 값으로 존재해야 함
* 외래 키의 값이 반드시 부모 테이블의 기본 키 일 필요는 없지만 유일한 값이여야 함 
```



### field

```python
* 필요 인자
참조하는 model class
on_delete 옵션
* migrate 작업 시 필드 이름에 _id를 추가하여 데이터베이스 열 이름을 만들어준다.

# articles/models.py
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
```



### on_delete

```
* 외래 키가 참조하는 객체가 사라졌을 때 외래 키를 가진 객체를 어떻게 처리할 지를 정의
* 데이터 무결성을 위해서 매우 중요한 결정
* 사용가능한 값들이 많지만
-CASCADE : 참조된 객체가 삭제 됐을 때 이를 참조하는 객체도 삭제
```



### 실습

```python
# articles/admin.py
from .models import Article, Comment
admin.site.register(Comment)

게시물을 만들고 댓글을 입력해야 오류가 안나고 실행됨
```



### 1:N 관계 related manager

### 역참조 (comment_set)

```
* ticle(1)-Comment(N)
* article.comment 형태로는 사용할 수 없고, article.comment_set manager가 생성됨
* 게시글에 몇 개의 댓글이 작성 되었는지 Django ORM이 보장할 수 없기 때문
```

### 참조(article)

```
* Comment(N)-Article(1)
* 댓글의 경우 어떠한 댓글이든 반드시 자신이 참조하는 게시글이 있으므로, comment.article과 같이 접근
```

### 실습(shell)

```sqlite
* 모든 댓글 조회하기(역참조, 1-N)
- article.comment_set.all() 
* 조회한 댓글 모두 출력
- for comment in comments:	
	print(comment.content)

* comment의 입장에서 참조하는 게시글 조회하기(참조, N-1)
- comment = Comment.objects.get(pk=1)
- comment.article
- comment.article.content
- comment.article_id
```



## Comment CREATE



### CommentForm 작성

```python
# articles/forms.py
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('article',)
        
# articles/views.py
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()    
    context = {
        'article': article,
        'comment_form':comment_form,        
    }
    return render(request, 'articles/detail.html', context)
```



### 댓글 작성

```python
# articles/urls.py 추가
path('<int:pk>/comments/', views.comments_create, name='comments_create'), 

# articles/views.py 추가
@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')
```

```django
# articles/detail.html
<form action="{% url 'articles:comments_create' article.pk %}" method="POST">
  {% csrf_token %}
  {{ comment_form }}
  <input type="submit">
  </form>
```



### save() method 

```python
* save(commit=False)
기본값은 True 되어 있지만 아직 데이터베이스에 저장되지 않은 인스턴스를 반환하기위해서는 False 값을 줌
저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용함
ex) 위의 comments_create 에서 사용됨
if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
        return redirect('articles:detail', article.pk)
```



## Comment READ

### 댓글 출력

```python
* 특정 article에 있는 모든 댓글을 가져온 후 context에 추가
# articles/views.py
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request, 'articles/detail.html', context)
```

```django
# articles/detail.html
{% for comment in comments %}
	<li>
      {{ comment.content }}      
    </li>
{% endfor %}
```



## Comment DELETE

### 댓글 삭제

```python
# articles/urls.py 추가
path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),

# articles/views.py 추가
@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
    return redirect('articles:detail', article_pk)
```

```django
# articles/detail.html
{% for comment in comments %}
    <li>
      {{ comment.content }}
      <form action=" {% url 'articles:comments_delete' article.pk comment.pk %}" method="POST" class="d-inline">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
    </li>
{% empty %}
  <p>댓글이 없어요</p>
{% endfor %}
```



## Comment 추가사항

### 댓글 개수 출력하기

```django
# articles/detail.html
{% if comments %}
    <p><b>{{ comments|length }}개의 댓글이 있습니다.</b></p>
  {% endif %}
```

### 댓글이 없는 경우 대체 컨텐츠 출력(DTL의 for-empty 태그 활용)

```django
{% for comment in comments %}
...
{% empty %}
  <p>댓글이 없어요</p>
{% endfor %}
```





## Custom User model

### User 모델 대체하기

```
* 일부 프로젝트에서는 Django 내장 User 모델이 제공하는 인증 요구사항이 적절하지 않을 수 있음
* Django는 User를 참조하는데 사용하는 AUTH_USER_MODEL 값을 제공하여, default user model을 재정의 할 수 있도록 함
* Django는 새 프로젝트를 시작하는 경우 기본 사용자 모델이 충분하더라도, 커스텀 유저 모델을 설정하는 것을 강력하게 권장
```



### AUTH_USER_MODEL

```
* User를 나타내는데 사용하는 모델
* 프로젝트가 진행되는 동안 변경할 수 없음
* 프로젝트 시작 시 설정, 참조하는 모델을 첫번째 마이그래이션에서 사용할수 있어야함
* 기본값은 'auth.User'
```



### Custom User 모델 정의하기

```python
* 관리자 권한과 함께 완전한 기능을 갖춘 User 모델을 구현하는 기본클래스인 AbstractUser를 상속받아 새로운 User 모델 작성
# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

