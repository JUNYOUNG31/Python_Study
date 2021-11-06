# Project_02

### 1.목표

* Python 기초 문법 실습
* 데이터 구조에 대한 분석과 이해
* 요청과 응답에 대한 이해
* API의 활용과 문서 분석



## A. 영화 개수 카운트 기능 구현

```python
tmdb_helper = TMDBHelper('0d9af9ec28d13f9cd2287cb2b89cd8ca') #나의 key 값 입력
url = tmdb_helper.get_request_url(region='KR',language='ko')
# method='/movie/popular' 는 default 값
# region 과 language 를 한국으로 설정

data = requests.get(url).json()   # requests 를 통해서 data 가져오기
return (len(data.get('results'))) # results의 개수 len 사용
```

* 학습한 내용

  * TMDBHelper 라는 직접 만든 class를 사용해서 정보를 가져오기
    * API Server 를 이용해서 데이터를 요청하고 가져오기
    * url 과 requests 사용하기

* 느낀점

  * url 과 requests 를 사용해서 많은 데이터를 가져오고

    거기서 필요한 정보를 가공하는 점에서 흥미를 느낌



## B. 영화 개수 카운트 기능 구현

```python
data = requests.get(url).json()    # requests 를 통해서 data 가져오기
high_vote_movie = [] # 평점높은 movie 값의 list 변수
for i in data.get('results'):      # results 중
    if i.get('vote_average') >= 8: # 평점이 8이상인 영화가 있다면
        high_vote_movie.append(i)  # 새로운 리스트에 추가
return high_vote_movie  		   # 추가된 movie 값 return
```

* 학습한 내용

  * TMDBHelper 라는 직접 만든 함수를 사용해서 정보를 가져오기

    * dict 의 list 의 dict 의 데이터에서 조건에 맞는 값 가져오기

      

* 느낀점

  * dict 과 list의 차이점을 알고 필요한 정보를 가져오는 것이 헷갈렸지만 이해했음

    

## C. 평점 순 정렬

```python
data = requests.get(url).json()   # requests 를 통해서 data 가져오기
sort_vote_movie = []              # 정렬할 movie list 변수

# 정렬하는데(정렬할 리스트, key는 한번사용할 함수 k: k의 평점, 높은값부터 정렬)
sort_vote_movie = sorted(data.get('results'), key=lambda k:k['vote_average'],reverse=True)

return sort_vote_movie[0:5]       # 5개까지만 출력하는 slice 이용
```

* 학습한 내용

  * TMDBHelper 라는 직접 만든 class를 사용해서 정보를 가져오기

    * dict 의 list 의 dict 의 데이터에서 조건에 맞는 값 가져오기

    * 정렬에서 높은 값부터 정렬  

      https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary  출처

      

* 느낀점

  * 이부분은 이해하기 좀 힘들점이 있었음

  * vote_average 로 정렬하기위해서 함수를 사용했음 

    

## D. 제목 검색, 영화 추천

```python
tmdb_helper =TMDBHelper('0d9af9ec28d13f9cd2287cb2b89cd8ca') #key 입력
movie_id = tmdb_helper.get_movie_id(title) # 제목입력해 movie_id 를 가져오기

# 추천영화를 나타내는 /movie/{movie_id}/recommendations 를 입력하고 한국으로 설정
url = tmdb_helper.get_request_url(f'/movie/{movie_id}/recommendations', region='KR',language='ko')
    
data = requests.get(url).json()           # requests 를 통해서 data 가져오기
movie_name = []                           # 이름을 저장할 list 변수 
try: # 예외처리를 통해서 검색할수 없을 경우 None 값 반환
    for i in data.get('results'):         # 값이 없을경우 반환하기위해 get 사용 
        movie_name.append(i.get('title')) # title값 추가
except:
    return None
return movie_name                         # 추가된 title 값의 list return
```

* 학습한 내용

  * TMDBHelper 라는 직접 만든 class를 사용해서 정보를 가져오기

    * dict 의 list 의 dict 의 데이터에서 조건에 맞는 값 가져오기

    * 값이 없을 때와 에러가 발생시 예외 처리를 통해 값을 반환

      

* 느낀점

  * try except 구문으로 예외가 발생하는 값에 대해서 None 값을 반환했다
  * 필요한 데이터를 가져오기위해 url 부분의 요청 메소드 변경하고 거기에 해당하는 정보를 가져오는 것에서 점점 익숙해지고 이해하는중

## E. 배우, 제작진 리스트 출력

```python
# 영화정보 나타내는 /movie/{movie_id}/credits 를 입력하고 한국으로 설정
url = tmdb_helper.get_request_url(f'/movie/{movie_id}/credits',language='ko')

data = requests.get(url).json() # requests 를 통해서 data 가져오기
actor_name = []     # 배우 이름을 저장할 list 변수 
crew_name = []      # 제작진 이름을 저장할 list 변수 
result = {}         # 배우와 제작진을 저장할 dict 변수
try:                # 예외처리를 통해서 검색할수 없을 경우 None 값 반환
    for i in data.get('cast'):
        if i.get('cast_id') < 10:             # cast_id 가 10 보다 작을 경우
            actor_name.append(i.get('name'))  # 이름을 list 에 추가
except:
    return None
try: # 예외처리를 통해서 검색할수 없을 경우 None 값 반환     
    for i in data.get('crew'): 
        if i.get('department') == 'Directing': # department = Directing 일 경우
            crew_name.append(i.get('name'))    # 이름을 list 에 추가
except:
    return None

# 배우와 제작진의 값을 result dict 에 추가       
result = {'cast' : actor_name, 'crew' :crew_name}

return result   # dict 값 return
```

* 학습한 내용

  * TMDBHelper 라고 직접 만든 class를 사용해서 정보를 가져오기

    * 값이 없을 때와 에러가 발생시 예외 처리를 통해 값을 반환

    * list 값을 dict 형태로 저장

      

* 느낀점

  * result 값에 예외처리를 하니 오류가 그대로 발생했다. 그래서 반복문의 시작부분에서 예외처리를 하니깐 실행이 되었다. 어디에 어떤 값이 반복되고 예외가 발생하는지에 대해 확실하게 알고 넘어가자



## F. 추가 정보 수집

해당하는 영화의 리뷰를 가져오는 함수 movie_review를 생성

```python
def movie_review(title):
    tmdb_helper =TMDBHelper('0d9af9ec28d13f9cd2287cb2b89cd8ca') #key 입력
    movie_id = tmdb_helper.get_movie_id(title) # 제목입력해 movie_id 를 가져오기
# 영화의 리뷰 나타내는 /movie/{movie_id}/reviews 를 입력  (한글 리뷰는 없다... ㅠㅠ)
    url = tmdb_helper.get_request_url(f'/movie/{movie_id}/reviews')
    data = requests.get(url).json()   # requests 를 통해서 data 가져오기    
    review_list = []                  # 리뷰를 저장할 list 변수
    try: # 예외처리를 통해서 검색할수 없을 경우 None 값 반환
        for i in data.get('results'):      
            review_list.append(i.get('content')) #review 내용 추가           
    except:
        return None
    
    return review_list                               # review 내용 return

if __name__ == '__main__':
    pprint(movie_review('Black Widow'))              # 블랙 위도우
    pprint(movie_review('Snowpiercer'))              # 설국열차
    pprint(movie_review('The Shawshank Redemption')) # 쇼생크 탈출
```

* 학습한 내용

  * TMDBHelper 라고 직접 만든 class를 사용해서 정보를 가져오기

    * 원하는 정보를 얻기 위해 직접 함수를 생성하기

    * 원하는 데이터를 얻기 위한 다른 요청 메소드 사용해보기

      

* 느낀점

  * 한글 리뷰를 가져오고 싶었는데 해당하는 영화에 언어를 한국으로 설정하니깐

    리뷰가 나오지않아 언어를 삭제하니 영어로는 값이 나왔다.

    해당하는 함수가 잘 작동하는 것을 확인해봄으로써 API 를 사용하는데 익숙해졌다.

