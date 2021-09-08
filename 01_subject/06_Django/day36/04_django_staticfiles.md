# day 36

## django managing static files

## Static file

### Static file

```
* 정적 파일
* 응답할때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
* Django에서는 이러한 파일들을 static file 이라함
```



### Static file 구성

```
1. django.contrib.staticfiles 가 INSTALLED_APPS 에 포함되어 있는지 확인
2. settings.py 에서 STATIC_URL을 사용
3. 템플릿에서 static 템플릿 태그를 사용하여 지정된 상대경로에 대한 URL을 빌드
   {% load static %}
   <img src="{% static 'my_app/image.jpg' %}" alt="sample image">
   
4. 앱의 static 폴더에 정적 파일을 저장  
   ex) my_app/static/my_app/image.jpg
```



### Django template tag

```
* load
  * 사용자 정의 템플릿 태그 세트를 로드
  * 로드하는 라이브러리, 패키지에 등록된 모든 태그와 필터를 로드
  
* static
  * STATIC_ROOT에 저장된 정적 파일에 연결 
  {% load static %}
  <img src="{% static 'my_app/image.jpg' %}" alt="sample image">
```



### staticfiles app

```
STATIC_ROOT 
	* collectstatic이 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로
	* django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아 넣은 경로
	* 개발 과정에서 setting.py의 DEBUG 값이 True로 설정되어 있으면 해당 값은 작용되지 않음
	* 실 서비스 환경에서 django의 모든 정적 파일을 다른 웹 서버가 직접 제공하기 위함
  
[참고]collectstatic
	* STATIC_ROOT에 정적 파일을 수집
      settings.py 에 작성
      STATIC_ROOT = BASE_DIR / 'staticfiles' 
 
      명령어
      $ python manage.py collectstatic 
```

```
STATIC_URL
	* STATIC_ROOT에 있는 정적파일을 참조 할 때 사용할 URL
	* 실제 파일이나 디렉토리가 아니며, URL로만 존재
	* 비어 있지 않은 값으로 설정한다면 반드시 / 로 끝나야 함
	
	STATIC_URL = '/static/'
```

```
STATICFILES_DIRS 
	* APP내에서 static 경로를 사용하는것 외에 추가적인 정적 파일 목록을 정의하는 리스트
	* 추가 파일 디렉토리에 대한 전체 경로를 포함하는 문자열 목록으로 작성되어야 함
	
	STATICFILES_DIRS = [
    BASE_DIR / 'static',
	]	
```



### Static files 사용하기 - 기본 경로

```django
app/static/app 경로 만들기

template에서 경로 참조
---주의사항 extends가 있다면 그 밑에 작성 extends 는 항상 최상위에 작성
{% extends 'base.html' %}  
{% load static %}
...
<img src="{% static 'articles/image1.jpg' %}" alt="sample image">
...
```



### Static files 사용하기 - 추가 경로

```django
project 와 같은 위치에 static/images 경로 만들기

settings.py 설정
STATICFILES_DIRS = [
BASE_DIR / 'static',
]

templates에서 경로 참조
{% load static %}
...
<img src="{% static 'images/image3.jpg' %}" alt="sample image second">
...
```



### Static files 사용하기 - STATIC_URL 확인

```
크롬 개발자 도구 확인가능 
```



## Media file

### Media file

```
* 미디어 파일
* 사용자가 웹에서 업로드하는 정적 파일(user-uploaded)
* 유저가 업로드한 모든 정적 파일
```



### Model field

```
ImageField
    * 이미지 업로드에 사용하는 모델 필드
    * FileField를 상속받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드를사용 가능
    * ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성 (max_length로 길이 변경 가능)

    * [주위]사용하려면 반드시 Pillow 라이브러리 필요
      pip install Pillow
```

```
FileField
    * 파일 업로드에 사용하는 모델 필드
    * 2개의 선택 인자를 가지고 있음
        1. upload_to
        2. storage -- 안배움	
```



### ImageField(or FileField)를 사용하기 위한 단계

```
1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정
2. upload_to속성을 정의하고 업로드 된 파일에 사용할 MEDIA_ROOT의 하위 경로 지정
3. 업로드된 파일의 경로는 django가 제공하는 'url'속성을 통해 얻음
```



### MEDIA_ROOT

```
* 사용자가 업로드한 파일들을 보관할 디렉토리의 절대 경로
* django는 파일을 데이터에베이스에 저장하지 않고 경로를 저장
* [주의] MEDIA_ROOT 와 STATIC_ROOT는 반드시 다른 경로로 지정

settings.py
MEDIA_ROOT =BASE_DIR / 'media'
```



### MEDIA_URL

```
* MEDIA_ROOT에서 제공되는 미디어를 처리하는 URL
* 업로드 된 파일의 URL을 만들어주는 역할
* 비어 있지 않은 값으로 설정한다면 반드시 / 로 끝나야함
* [주의] MEDIA_URL와 STATIC_URL는 반드시 다른 경로로 지정

settings.py
MEDIA_URL = '/media/'
```



### 개발 단계에서 사용자가 업로드 한 파일 제공하기

```python
사용자가 업로드한 파일이 프로젝트에 업로드되지만, 
실제로 사용자에게 제공하기 위해서는 업로드된 파일의 URL 필요
crud/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings				# 추가	
from django.conf.urls.static import static      # 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 추가

# 업로드 된 파일의 URL == settings.MEDIA_URL
# 위 URL을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT
```



## Image Upload (CREATE)

### ImageField 작성

```python
* upload_to='images/'
	* 실제 이미지가 저장되는 경로 지정
* blank=True
	* 빈 값이 허용되도록 설정
	
articles/models.py
class Article(models.Model):
	image = models.ImageField(upload_to='images/', blank=True) # 추가
    
모델을 변경했기 때문에 makemigrations 와 migrate 실행
```



### Model field option - "blank"

```
* 기본 값 : False
* True 인 경우 필드를 비워 둘 수 있음. DB에는 ''빈문자열이 저장
* 유효성 검사에서 사용됨(is_valid)
	*필드에 blank=True가 있으면 form 유효성 검사에서 빈 값을 입력할 수 있음
```



### Model field option - "null"

```
* 기본 값 : False
* True면 django는 DB에 null을 저장
* 주의사항
	* 문자열 기반 필드에는 사용하는 것을 피해야 한다.
	* 문자열 기반 필드에 True로 설정 시 '데이터없음'에 빈문자열과 NULL의 2가지 가능한 값이 있음을 의미
	* 대부분의 경우 '데이터없음'에 대해 두가지 가능한 값을 갖는 것은 중복되며,
	  Django는 NULL이 아닌 빈 문자열을 사용하는 것이 규칙
```



### blank & null

```python
* blank => Validation-related
* null  => Database-related

* 문자열 기반 및 비문자열 기반 필드 모두에 대해 null option은 DB에만 영향을 미치므로,
  form에서 빈 값을 허용하려면 blank=True를 설정해야 함
  
models.py

class Person(models.Model):
	name = models.CharField(max_length=10)
	
	#null=True 금지
	bio =  models.TextField(max_length=50, blacnk=True)
	
	#null, blank 모두 설정 가능 -> 문자열 기반 필드가 아니기 때문
	birth_date =  models.DateField(null=True, blacnk=True)
```



### form 요소 - enctype(인코딩) 속성 - articles/create.html 수정

```django
게시글 작성 form enctype 속성 지정
<form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">

1. multipart/form-data
* 파일/이미지 업로드 시에 반드시 사용해야 함(전송되는 데이터의 형식을 지정)
* <input type="file">을 사용할 경우에 사용


--- 안배움
2. application/x-www-form-urlencoded
* (기본값) 모든 문자 인코딩

3. text/pain
* 인코딩을 하지 않은 문자 상태로 전송
* 공백은 '+' 기호로 변환하지만, 특수 문자는 인코딩 하지 않음
```



### input 요소 - accept 속성

```
* 입력 허용할 파일 유형을 나타내는 문자열
* 쉼표로 구분된 " 고유 파일 유형 지정자"(unique file type spectifiers)
* 파일 검증을 하는 것은 아님
  (이미지만 accept해 놓아도 비디오나 오디오 파일을 제출할 수 있음)
  파일 업로드 시 허용할 파일 형식에 대해 자동으로 필터링	
 
* 고유 파일 유형 지정자
	*<input type="file">에서 선택할 수 있는 파일의 종류를 설명하는 문자열
```



### Views.py 수정

```python
* 업로드한 파일은 request.FILES 객체로 전달됨

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES) # FILES 부분 추가
        # form = ArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```



### DB 및 파일 트리 확인

```
* 실제 파일 위치 => MEDIA_ROOT/images/

* DB에 저장된것은 파일의 경로가 저장된다
```



## Image Upload (READ)

### 이미지 경로 불러오기

```
* article.img.url == 업로드 파일의 경로
* article.image == 업로드 파일의 파일이름

detail.html
...
<img src="{{ article.image.url }}" alt="{{ article.image }}">
...

image가 뜨는지 확인하고 개발자 도구를 활용해서 MEDIA_URL 확인하기
```



### STATIC_URL 과 MEDIA_URL

```
* static, media 모두 서버에 요청해서 조회
* 서버에 요청하기 위한 URL을 urls.py가 아닌 settings에 먼저 작성 후 urlpatterns에 추가하는 형식
```



## Image Upload (UPDATE)

### 이미지 수정하기

```
* 이미지는 바이너리 데이터(하나의 덩어리)이기 때문에 텍스트처럼 일부만 수정하는 것은 불가능
* 새로운 사진으로 덮어 씌우는 방식을 사용
```



### form 요소 - enctype(인코딩) 속성 - articles/update.html 수정

```django
<form action="{% url 'articles:update' article.pk %}" method="POST" enctype="multipart/form-data">
    
```



### Views.py 수정

```python
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article) # 추가
        #  form = ArticleForm(request.POST, instance=article, files=request.FILES)
        # 												      뒤에 넣을려면 인자를 지정
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```



### detail.html 수정 - 이미지를 넣지 않을 경우의 처리

```django
...
{% if article.image %}
    <img src="{{ article.image.url }}" alt="{{ article.image }}">
{% else %}
    <img src=" {% static 'images/image4.png' %}" alt="default image">
{% endif %}
...
```



### upload_to argument

```python
업로드 디렉토리와 파일 이름을 설정하는 2가지 방법
1. 문자열 값이나 경로 지정
	* 파이썬의 strftime() 형식이 포함될 수 있으며, 이는 파일 업로드 날짜/시간으로 대체 됨

models.py
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # MEDIA_ROOT/images/ 경로로 파일 업로드
    image = models.ImageField(upload_to='images/', blank=True)
    # MEDIA_ROOT/2021/09/08/ 경로로 파일 업로드
    image = models.ImageField(upload_to='%Y/%m/%d/', blank=True)
    

2. 함수 호출
     * 반드시 2개의 인자를 사용
        1. instance
        2. filename
        

models.py

def articles_image_path(instance, filename):
    # MEDIA_ROOT/user_<pk>/ 경로로 <filename> 이름으로 업로드
    return f'user_{instance.pk}/{filename}'

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()    
    # image = models.ImageField(upload_to='%Y/%m/%d/', blank=True)
    image = models.ImageField(upload_to=articles_image_path, blank=True)
```



## Image Resizing

### 이미지 크기 변경하기

```
* 실제 원본 이미지를 서버에 그대로 업로드 하는 것은 서버의 부담이 큰 작업
* <img> 태그에서 직접 사이즈를 조정할 수 도 있지만 (witdh 와 height),
  업로드 될 때 이미지 자체를 resizing 하는 것을 사용해 볼 것
* django-imagekit 라이브러리 활용
```

```python
1. django-imagekit 설치
$ pip install django-imagekit

2. INSTALLED_APPS 추가
settings.py 설정
INSTALLED_APPS = [
	...
	'imagekit', 
	...
]
```

```
* 원본 이미지를 재가공하여 저장(원본x 썸네일o)

models.py
from django.db import models
from imagekit.models import ProcessedImageField  # 추가
from imagekit.processors import ResizeToFill     # 추가

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()    
    image = ProcessedImageField(
        upload_to='thumbnails/',
        processors=[ResizeToFill(100,50)],
        format='JPEG',
        options={'quality: 60'}
    )
```

