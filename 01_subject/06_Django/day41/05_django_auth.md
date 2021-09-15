# day 41

## django auth

## Authentication System 1

### The Django Authentication System

```
* Django 인증 시스템은 django.contrib.auth에 Django contrib module로 제공
* 필수 구성은 settings.py에 이미 포함되어 있음
  INSTALLED_APPS = [ 'django.contrib.auth','django.contrib.contenttypes', ]
  
* django.contrib.auth =>> 인증 프레임워크의 핵심과 기본 모델을 포함
* django.contrib.contenttypes =>> 사용자가 생성한 모델과 권한을 연결할 수 있음

* Django 인증 시스템은 인증(Authentication)과 권한(Authorization) 부여를 함께 제공

* 인증(Authentication)
	* 신원 확인
	* 사용자가 자신이 누구인지 확인하는 것

* 권한(Authorization)
	* 권한 부여
	* 인증된 사용자가 수행할 수 있는 작업을 결정
```



### 두번째 앱 (accounts) 생성하기

```python
$ python manage.py startapp accounts

* app 이름이 반드시 accounts 일 필요는 없지만 auth와 관련해 
  django 내부적으로 accounts 라는 이름으로 사용되고 있기 때문에 accounts로 지정을 권장
  
# settings.py 추가 
INSTALLED_APPS = [ ...'accounts',... ]
  
# crud/urs.py 추가
urlpatterns = [ ... path('accounts/', include('accounts.urls')), ... ]
  
# accounts/urls.py 생성 및 추가
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [ ]
```





## 쿠키와 세션

### HTTP  특징

```
* 비연결지향 (connectionless)
	* 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
* 무상태 (stateless)
	* 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
	* 클라이언트와 서버가 주고 받는 메세지들은 서로 완전히 독립적임

* < 클라이언트와 서버의 지속적인 관계를 유지하기 위해 쿠키와 세션이 존재 > 
```



### 쿠키 ( Cookie) 개념

```
* 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
* 사용자가 웹사이트를 방문할 경우 해당 웹사이트의 서버를 통해 사용자의 컴퓨터에 설치되는 
  작은 기록 정보 파일
  	* 브라우저는 쿠키를 로컬에 KEY-VALUE의 데이터 형식으로 저장
  	* 저장한 뒤, 동일한 서버에 재요청 시  저장된 쿠키를 함께 전송

* HTTP 쿠키는 상태가 있는 세션을 만들어 준다
* 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용
	* 이를 이용해 사용자의 로그인 상태를 유지
	* 상태가 없는(stateless)HTTP 프로토콜에서 상태 정보를 기억 시켜주기 때문

* < 웹 페이지에 접속하면 요청한 웹 페이지를 받으며 쿠키를 저장하고, 클라이언트가 같은 서버에 
	재요청 시 요청과 함께 쿠키도 함께 전송 > 

* [참고] 소프트웨어가 아니라서 악성코드를 설치할 수 없지만, 사용자의 행동 추적과 쿠키를 훔쳐 
		해당 사용자의 계정 접근권한을 획득할 수도 있음
```



### 요청과 응답

```
1. The browser requests a web page
2. The server sends the page and the cookie
3. The browser requests another page from the same server
```



### 쿠키의 사용 목적

```
1. 세션 관리 (Session management) 
   로그인, 아이디 자동 완성, 공지 하루 안보기, 팝업 체크, 장바구니 등의 정보 관리

2. 개인화 (Personalization)
   사용자 선호, 테마 등의 설정

3. 트래킹 (Tracking)
   사용자 행동을 키록 및 분석
```



### 세션 (Session)

```
* 사이트와 특정 브라우저 사이의 "상태(state)"를 유지시키는 것
* 클라이언트가 서버에 접속하면 서버가 특정 session id 를 발급하고, 발급 받은 session id를 쿠키에 저장
	* 클라이언트가 다시 서버에 접속하면 요청과 함께 쿠키(session id가 저장된)를 서버에 전달
	* 쿠키는 요청 때마다 서버에 함께 전송되므로 서버에서 session id를 확인해 알맞은 로직을 처리
* ID는 세션을 구별하기 위해 필요하며, 쿠키에는 ID만 저장함
```



### 쿠키 lifetime (수명)

```
* 쿠키의 수명은 두가지 방법으로 정의
1. Session cookies
	* 현재 세션이 종료되면 삭제
	* 브라우저가 "현제 세션 (current session)"이 종료되는 시기를 정의
		* [참고] 일부 브라우저는 다시 시작할 때 세션 복원 (session restoring)을 사용해
				세션 쿠기가 오래 지속 될 수 있도록 함

2. Persistent cookies (or Permanent cookies)
	* Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제
```



### Session in Django

```
* Django의 세션은 미들웨어를 통해 구현됨
* Django는 database-backed sessions 저장 방식을 기본 값으로 사용
* Django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 세션을 알아냄
	* 세션 정보는 Django DB의 django_session 테이블에 저장
* 모든 것을 세션으로 사용하려고 하면 사용자가 많을 때 서버에 부하가 걸릴 수 있다
```



### Authentication System in MIDDLEWARE

````
* SessionMiddleware =>> 요청 전반에 걸쳐 세션을 관리
* AuthenticationMiddleware =>> 세션을 사용하여 사용자를 요청과 연결

settings.py에 이미 포함되어 있음
  MIDDLEWARE = [ 'django.contrib.sessions.middleware.SessionMiddleware',
  				 'django.contrib.auth.middleware.AuthenticationMiddleware', ]
  				 
[참고] MIDDLEWARE(미들웨어)
* http 요청과 응답 처리 중간에서 작동하는 시스템(hooks)
* django는 http 요청이 들어오면 미들웨어를 거쳐 해당 URL에 등록되어 있는
  view로 연결해주고, http 응답 역시 미들웨어를 거쳐서 내보냄
* 주로 데이터 관리, 애플리케이션 서비스, 메시징, 인증 및 API 관리를 담당
````



## 로그인

### 로그인

```
* 로그인은 Session을 Create하는 로직과 같음
* Django는 인증에 관한 built-in forms를 제공
```



### AuthenticationForm

```
* 사용자 로그인을 위한 form
* request를 첫번째 인자로 가짐
```



### login 함수

```
* login(request, user, backend=None)
	* 현재 세션에 연결하려는 인증 된 사용자가 있는 경우 login()함수가 필요
	* 사용자를 로그인하며 view 함수에서 사용
	* HttpRequest 객체와 User 객체가 필요
	* django의 session framework를 사용하여 세션에 user의 ID를 저장(==로그인)
```



```python
# accounts/urls.py
urlpatterns = [ path('login/', views.login, name='login'), ]

# account/login.html 생성 및 추가
{% extends 'base.html' %}
{% block content %}
  <h1>LOGIN</h1>
  <form action="{% url 'accounts:login' %}" method="POST">
  ...
{% endblock content %}

# accounts/views.py
from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login  ## login 이 겹쳐서 혼동방지
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인!
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```



### get_user( )

```
* AuthenticationForm의 인스턴스 메서드
* user_cache는 인스턴스 생성 시에 None으로 할당되며 유효성검사 통과 시 로그인한 사용자 객체를 할당
* 인스턴스의 유효성을 먼저 확인하고, 인스턴스가 유효할 때만 user를 제공
```



## Authentication data in templates

## 현재 로그인 되어있는 유저 정보 출력

```
# base.html
<h3>Hello, {{ user }}</h3>

* context processors
	* 템플릿이 렌더링 될 때 자동으로 호출 가능한 컨텍스트 데이터 목록
	* 작성된 프로세서는 RequestContext에서 사용 가능한 변수로 포함

* Users
	* 템플릿 RequestContext를 렌더링할 때, 현재 로그인한 사용자를 나타내는 auth.User 인스턴스
	는 템플릿 변수 {{ user }}에 저장
	
# settings.py
TEMPLATES = [
    { ...'OPTIONS': 
    { 'context_processors': 
    [ ... 'django.contrib.auth.context_processors.auth',... ],},},]
```



## 로그아웃

### 로그아웃

```
* 로그아웃은 Session을 Delete하는 로직과 같음
```



### logout 함수

```
* logout(request)
	* HttpRequest 객체를 인자로 받고 반환 값이 없음
	* 사용자가 로그인하지 않은 경우 오류를 발생시키지 않음
	* 현재 요청에 대한 session data를 DB에서 완전히 삭제하고, 클라이언트 쿠키에서도 session id가 삭제
	* 다른사람이 동일한 웹 브라우저를 사용하여 로그인하고, 이전 사용자의 세션 데이터에 엑세스하는것을 방지
```



## 로그인 사용자에 대한 접근 제한

###  Limiting access to logged-in users

```
* 2가지 방법
1. The raw way
	* is_authenticated 속성
2. The login_required 

```







## Authentication System 1

## 회원가입

### UserCreationForm

```
* 주어진 username과 password로 
```

