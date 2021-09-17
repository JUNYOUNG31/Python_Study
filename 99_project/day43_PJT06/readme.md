#### 후기

- 박**

```
이번 프로젝트는 이때까지 했던 프로젝트에 사용자를 등록하고 인증을 통해서 서비스에 접근 권한을 부여하고 사용자가 아니라면 접근을 못하도록 설정하는 단계를 추가하였다. review를 수정하고 삭제를 추가했는데 인증하지 않았을때도 기능이 수행되었기 때문에 login_required 기능을 이용해서 접근하지 못하도록 설정했다.
어려웠던 점은 아직까지 from import 구문이 머리에 팍팍 들어오지 않는다. 아직까지 옆에 배웠던 내용들을 올려두고 막히는 부분에서는 보고 작성하는중인데 시험전까지는 안보고 지금까지 했던 기능들을 추가하도록 해야겠음
```

- 박**

```
오전에 git branch 에 대해 배웠지만 이번 프로젝트는 저번 프로젝트와 같이 네비게이터와 드라이버로 나누어 진행하였습니다. 제가 accounts의 드라이버를, **님이 community의 드라이버를 맡았습니다.
드라이버를 맡아 코드를 진행할 때는 머리속에 남아있는 코드와 **님의 지시에 따라 진행하면 되어 편하게 진행할 수 있었지만 제가 네이게이터를 맡아 진행할 때는 이게 맞나...? 저게 맞나...? 싶고 평소 혼자서 했었더라면 모르겠으면 일단 해보고 오류가 났구나...하고 다시 했던것도 조금이라도 오류를 덜 내기 위해 좀 더 꼼꼼히 보게 되었던 것 같습니다.
혼자 진행하면 오타를 너무 많이 내서 진행이 엄청나게 느려지는데 페어로 진행하며 오류가 적어져서 시간이 많이 절약되는 것 같습니다. 혼자서 프로젝트를 할 때도 타자 치는 그 순간순간 오타체크를 잘 해야겠다는 생각이 듭니다.
```



#### 진행과정

- 박**

##### 1. 공유 템플릿 생성 및 사용

```html
</head>
<body>
  <nav class="nav">  
    <a class="nav-link" href="{% url 'community:index' %}">INDEX</a>
    {% if request.user.is_authenticated %}
      <a class="nav-link" href="{% url 'community:create' %}">CREATE</a>
      <form action="{% url 'accounts:logout' %}"method="POST">
        {% csrf_token %}
        <input type="submit"value="LOGOUT" class="nav-link">
      </form>
    {% else %}
      <a class="nav-link" href="{% url 'accounts:login' %}">LOGIN</a>
      <a class="nav-link" href="{% url 'accounts:signup' %}">SIGNUP</a>
    {% endif %}
  </nav>
  <div class="container">
    {% block content %}  
    
    {% endblock content %}
  </div>
</body>
```

- 로그인시 INDEX, CREATE, LOGOUT이 로그인 상태가 아닐 경우 LOGIN, SIGNUP이 출력되도록 하였습니다

  

##### 2. 신규 사용자 생성

```python
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('community:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('community:index')
    else:
        form = UserCreationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/signup.html',context)
```

- GET, POST일 때 코드 실행 되도록 하였습니다
- 로그인 된 상태라면 community:index로 가도록 하였습니다
- UserCreationForm import하여  form을 받아와서 signup.html에서 해당 form을 사용합니다

##### 3. 기존 사용자 인증(로그인)

```python
def login(request):
    if request.user.is_authenticated:
        return redirect('community:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('community:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/login.html',context)
```

- 로그인 된 상태라면 community:index로 가도록 하였습니다
- AuthenticationForm을 사용하여 login.html에서 form을 사용했습니다

##### 4. 인증된 사용자 인증해제

```python
@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('community:index')
```

- is_authenticated로 로그인 된 사용자를 받아 로그아웃 한 후 index로 이동합니다.





- 박**

v. 새로운 리뷰 작성

```python
# views.py - create
@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form
    }
    return render(request, 'community/create.html', context)

# create.html
...
<form action="{% url 'community:create' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>
...

여기에서 로그인에 대한 관련여부를 주지 않아도 base에서 먼저 인증을 하기 때문에 따로 필요없는것 같다
```



vi. 전체 리뷰 목록 조회

```python
# views.py - index

def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews':reviews
    }
    return render(request, 'community/index.html', context)

# index.html
...
{% for review in reviews %}  
  <p>{{ review.pk }} 번글 :
   <a href="{% url 'community:detail' review.pk %}"> {{ review.movie_title }}</a>
  </p> 
{% endfor %}
...

index 에서는 크게 어려운점은 없었음 pk를 불러서 가져오고 a 태그로 링크를 걸어주었고 글번호도 추가해줬다
```



vii. 단일 리뷰 상세 조회

```python
# views.py - detail
@login_required
def detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    context = {
        'review':review
    }
    return render(request, 'community/detail.html', context)

# detail.html
...
  <p>영화제목: {{ review.movie_title }}</p>
  <p>제목: {{ review.title }}</p>
  <p>내용: {{ review.content }}</p>
  <p>평점: {{ review.rank }}</p>
    
  <a href="{% url 'community:update' review.pk %}">UPDATE</a>
  <form action="{% url 'community:delete' review.pk %}"method="POST">
    {% csrf_token %}
    <input type="submit"value="DELETE">
  </form>
...

마지막에 수정과 삭제 버튼을 추가하지 않아서 뒤늦게 추가해줬고 그 과정에서 사용자 인증여부 기능을 추가하지 않아서 그것도 추가해줬다.
```



viii. 기존 리뷰 수정

```python
# views.py - update
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'review':review,
        'form':form,
    }
    return render(request, 'community/update.html', context)

# update.html
...
<form action="{% url 'community:update' review.pk %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>
...

update 에서는 해당하는 pk의 내용을 불러와야해서 pk 를 넣어주었고 기존의 했던 방법과 동일하게 구현하였다.
```



ix. 리뷰 데이터 삭제

```python
# views.py - delete

@login_required
@require_POST
def delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    return redirect('community:index')

처음에는 delete 에는 기본적으로 login_required 가 들어가야된다고 생각했는데 이미 detail 에서 로그인 하지 않을 경우 접근하지 못하도록 설정해놨기 때문에 굳이 delete에 추가하지 않아도 될것같다.
```

