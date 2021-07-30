# day10

## 관통 프로젝트_02

### CLI

requests

BeautifulSoup

```python
import requests
from bs4 import BeautifulSoup

#요청을 보낼 URL
url = 'https://finance.naver.com/sise/'

# 실제 요청을 보내고 , 응답 객체를 response 변수에 저장
response = requests.get(url)

#응 답 객체의 본문(text)을 해석하여 data 변수에 저장
data = BeautifulSoup(response.text,'html.parser')

# 해석한 data에서 원하는 정보를 선택하고, 내용만 kospi에 저장
kospi =data.select_one('#KOSPI_NOW').text

print(kospi)
```



---

### API

응용 프로그램을 위한 접점

### API Server 

응용 프로그램을 위한 데이터를 응답하는 프로그램



### API 로 부터 데이터 받아보기

```python
import requests

#요청을 보낼 URL
url = 'https://api.agify.io?name=michael'

#응답 json str을 dict 로 파싱해서 response에 저장
response = requests.get(url).json()

print(response['age'])
print(response)
```



## Project 안내

### 최종목표

영화 추천 서비스를 제공하는 커뮤니티 서비스 설계



### TMDB = THE MOVIE DB  에서 데이터 가져오기

TMDB DEVELOPER 에서 가져온다

https://developers.themoviedb.org/3/getting-started/introduction



필요한 값을 얻기위해 제공되는 보기들을 잘 살펴서 이용하자

```python
https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>
    									#발급받은 본인의 api key 값 넣기
        
#인기작을 뽑고 싶다
https://api.themoviedb.org/3/
#인기작의 정보를 가져오는 get popular
movie/popular
?
api_key=본인키
&
language=ko   #언어 설정은 선택
&
region=KR	  # 지역 설정
```



 