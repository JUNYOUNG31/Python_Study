# day 64

## DB

## REST API



## HTTP 

### 복습

```
웹에서 이루어지는 모든 데이터 교환의 기초
* 요청 - 클라이언트에 의해 전송되는 메세지
* 응답 - 서버에서 응답으로 전송되는 메세지

request methods
* 자원에 대한 행위를 정의
* GET, POST, PUT, DELETE

response status codes
* 요청이 성공적으로 완료되었는지 여부를 나타냄
* 응답은 5개의 그룹으로 나뉘어짐
1. Imformational responses(1xx)
2. Successful responses(2xx)
3. Redirection responses(3xx)
4. Client error responses(4xx)
5. Server error  responses(5xx)

URL, URN
URL
* 통합 자원 위치
* 네트워크 상에 자원이 어디 있는지 알려주기 위한 약속
* 웹주소 링크라고도 불림

URN
* 통합 자원 이름
* URL 과 달리 자원의 위치에 영향을 받지않는 유일한 이름 역할을 함
* ex) ISBN(국제표준도서번호)

URI
* 통합 자원 식별자
* 인터넷의 자원을 식별하는 유일한 주소 (정보의 자원을 표현)
* 인터넷에서 자원을 식별하거나 이름을 지정하는데 사용되는 간단한 문자열
* 하위 개념이 URL 과 URN
* URI는 크게 URL 과 URN으로 나뉘지만 URN 비중이 매우 작아서 URL은 URI와 같은 의미처럼 사용하기도 함
```



### URI 의 구조

```
https://www.example.com:80/path/to/myfile.html/?key=value#quick-start
```

```
Scheme(protocol)
* 브라우저가 사용해야 하는 프로토콜
* Http(s), data, file, ftp, malito

https://
```

```
Host(Domain name)
* 요청을 받는 웹 서버의 이름
* IP address를 직접 사용할 수도 있지만, 실 사용시 불편하므로 웹에서 그리 자주 사용되지는 않음.
  (google의 IP address - 142.251.42.142)

www.example.com
```

```
Port
* 웹 서버 상의 리소스에 접근하는데 사용되는 기술적인 '문(gate)'
* Http 프로토콜의 표준 포트
- HTTP 80
- HTTPS 443

:80
```

```
Path
* 웹 서버 상의 리소스 경로
* 초기에는 실제 파일이 위치한 물리적 위치를 나타냈지만, 현재 물리적인 실제 위치가 아닌 추상화 형태의 구조로 표현

/path/to/myfile.html
```

```
Query(Identifier)
* Query String Parameters
* 웹 서버에 제공되는 추가적인 매개 변수
* & 로 구분되는 key-value 목록

/?key=value
```

```
Fragment
* Anchor
* 자원 안에서의 북마크의 한 종류를 나타냄
* 브라우저에게 해당 문서(HTML)의 특정 부분을 보여주기 위한 방법
* 브라우저에게 알려주는 요소이기 때문에 부분 식별자라고 부르며 # 뒤의 부분은 요청이 서버에 보내지지 않음

#quick-start
```



## RESTful API

### API

```
* Application Programming Interface
* 프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스
* Web API
- 현재 웹 개발은 모든 것을 직접 개발하기 보다 여러 open API를 활용하는 추세
* 응답 데이터 타입
- HTML, XML, JSON 등
ex) 유튭 파파고 카카오맵 등등
```

### REST

```
* REpresentational State Transfer
* API server를 개발하기 위한 일종의 소프트웨어 설계 방법론
* 네트워크 구조 원리의 모음
* REST 원리를 따르는 시스템을 RESTful 이란 용어로 지칭

* REST의 자원과 주소의 지정방법
1. 자원 - URI
2. 행위 - HTTP method
3. 표현 - 자원과 행위를 통해 궁극적으로 표현되는 (추상화된) 결과물
	   - JSON으로 표현된 데이터를 제공
	   
* REST의 핵심 규칙
1. '정보'는 URI로 표현
2. 자원에 대한 '행위'는 HTTP method로 표현(GET, POST, PUT, DELETE)

* 설계 방법론은 지키지 않았을때 잃는 것보다 지켰을 때 얻는 것이 훨씬 많음
```

### JSON(JavaScript Object Notation)

```
특징
* 사람이 읽거나 쓰기 쉽고 기계가 파싱(해석,분석)하고 만들어내기 쉬움
* 파이썬의 dictionary, 자바스크립트의 object처럼 C 계열의 언어가 갖고 있는 자료구조로 쉽게 변화할 수 있는 key_value 형태의 구조를 가짐
```



## Response

### django-seed

```
django-seed 라이브러리를 사용해 모델 구조에 맞는 데이터를 랜덤으로 생성
설치 pip install django-seed
python manage.py seed appname --number=20
```



### 1.Response - HTML

```python
# HTML을 응답하는 서버
# urls.py 추가
path('html/', views.article_html),

# views.py
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article.html', context)
```



### 2.Response - JsonResponse

```python
# JsonResponse 객체를 활용한 JSON 데이터 응답
# urls.py 추가
path('json-1/', views.article_json_1),

# views.py
def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                'created_at': article.created_at,
                'updated_at': article.updated_at,
            }
        )
    return JsonResponse(articles_json, safe=False)
```

```
Content-type entity header
* 데이터의 media type(MIME type, content type)을 나타내기 위해 사용됨
* 응답 내에 있는 컨텐츠의 유형이 실제로 무엇인지 클라이언트에게 알려줌

JsonResponse objects
* JSON-encoded response를 만드는 HttpResponse의 서브 클래스
* 'safe' parameter
- True(기본값)
- dict 이외의 객체를 직렬화(serialization)하려면 False로 설정
```



### Serialization

```
직렬화
* 데이터 구조나 객체 상태를 동일하거나 다른 컴퓨터 환경에 저장하고, 나중에 재구성할 수 있는 포맷으로 변환하는 과정

Serializers in Django
Queryset 및 Model Instance와 같은 복잡한 데이터를 JSON. XML 등의 유형으로 쉽게 변환 할 수 있는 Python 데이터 타입으로 만들어줌
```



### 3. Response - Django Serializer

```python
# Django의 내장 HttpResponse를 활용한 JSON 응답
# 주어진 모델 정보를 활용하기 때문에 이전과 달리 필드를 개별적으로 직접 만들어 줄 필요 없음
# urls.py 추가
path('json-3/', views.article_json_3),

# views.py
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers

def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')
```



### 4. Response - Django REST Framework

```
Django REST framework(DRF) 라이브러리를 사용한 JSON 응답
설치 pip install djangorestframework
```

```python
# urls.py 추가
path('json-3/', views.article_json_3),

# Article 모델에 맞춰 자동으로 필드를 생성해 serialize 해주는 ModelSerializer 확인
# serializers.py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
                
# views.py 추가
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer
# @api_view(['GET'])
@api_view()
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
```



### Django REST Framework(DRF)

```
* Web API 구축을 위한 강력한 Toolkit을 제공하는 라이브러리
* DRF의 Serializer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 구성되고 작동함

```



