# Project_01

## A . 제공되는 영화 데이터의 주요내용 수집

```python
  'name' : movie.get('name') # get은 none 반환
# 'name' : movie['name']     # 에러 발생
```

* 학습한 내용

  * get 을 통해 데이터를 불러오는 것과 [] 를 사용해 불러 오는것의 차이
    * get 을 사용하면 에러가 발생하지 않고 none 값을 출력
    * [] 을 사용하면 데이터가 존재하지 않을 경우에 에러가 발생

* 느낀점

  * 원하는 데이터를 가져오는데 큰 어려움은 없었음

    하지만 불러온 값들을 응용해서 다음 과제를 해결할려면 계속 연습해야할 듯



## B. 제공되는 영화 데이터의 주요내용 수정

```python
genre_names =[]  #genre의 이름  
    for g_id in genres: # genres의 id
        for m_id in movie['genre_ids']: # movie의 id
            if g_id['id'] == m_id:
                genre_names += [g_id['name']]   
```

* 학습한 내용

  * list에서 해당하는값과 다른 list에서 해당하는 값 비교하기
    * 같은 값이 있다면 해당하는 id 의 name 을 출력

* 느낀점

  * 2중 for문 밖에 생각나지 않아서 2중 for문을 사용함

    list의 값들을 불러오는데 시간이 좀 걸림

## C. 다중 데이터 분석 및 수정

```python
def movie_info(movies, genres):
    #여기에 코드를 작성합니다.  
    movie_all =[]  # 모든 movie를 불러오는 list
    for movie_name in movies: 
    #생략
movie_all += [detail]  # 앞의 problem_b.py 의 값들을 더해준다
```
* 학습한 내용

  * movies의 모든 값들의 필요한 정보만 뽑아 온다.

    * for 문을 통해 앞의 problem_b.py 의 값들을 불러온 후

      movie_all 값에 더해준다

* 느낀점

  * return 의 위치와 더할 값들의 형태에 따라서 출력되는 값이 다양하게 바뀌므로

    주의 깊게 확인할 필요가 있음

## D. 알고리즘을 통한 데이터 출력

```python
def max_revenue(movies):    
    # 여기에 코드를 작성합니다. 
    movie_max = 0  # revenue의 최대값을 받는 변수  
    movie_name = '' # 최대값에 해당하는 영화제목을 받는 변수
    for movie in movies:        
        movie_id =movie['id'] # id 값을 가져오고     
        revenue_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        revenue_list = json.load(revenue_json)   # json 파일과 연결하기
        if  revenue_list['revenue'] > movie_max: 
            movie_max = revenue_list['revenue']  # max 값을 갱신하기
            movie_name = revenue_list['title']   # max 값에 해당하는 제목을 받기
    return movie_name
```

* 학습한 내용

  * open과 json.load 를 통해 폴더에 접근해서 파일과 연결하는 법
  * 불러온 데이터 값을 비교하여 새로운 값을 갱신

* 느낀점

  * 해당 폴더에 있는 json 파일의 값을 불러오는데 어려움을 겪었지만 

    동기들의 도움으로 어려움을 극복할 수 있었음

## E. 알고리즘을 통한 데이터 출력

```python
if month_list['release_date'][5:7] == '12':
   # 해당하는 월을 받기 위해 slicing 사용하기           
            movie_name += [month_list['title']]  #해당하는 영화이름 받아서 추가하기
    return movie_name
```

* 학습한 내용
  * 날짜를 가져와서 월에 해당하는 데이터만  뽑아내기 위해 slicing 사용
* 느낀점
  * 앞의 problem_d.py 를 해결한 후 이해하고 problem_e.py 를 해결하니 충분히 해결할 수 있었다.

