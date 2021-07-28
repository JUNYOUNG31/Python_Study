import json
# A 
# 특정 데이터만을 가져오는 법
movie = []

movie.get('name')  # get 은 none 값을 반환
movie['name']      # 에러가 발생

# B
# 리스트의 값과 다른 리스트의 값을 비교
genres =[]
genre_names = []
for i in genres:
    if i.get('id') in movie.get('genre_ids'):
        genre_names += [i.get('name')]    
#for 문을 한번 사용

genre_names =[]  #genre의 이름  
for g_id in genres: # genres의 id
    for m_id in movie['genre_ids']: # movie의 id
        if g_id['id'] == m_id:
            genre_names += [g_id['name']]   
#내가 한 2중 for문

# C 위의 불러온 값을 리스트로 나열하기
def movie_info(movies, genres):    
    movie_all =[]  # 모든 movie를 불러오는 list  
    detail = []    # B 의 값
    movie_all += [detail]  # 앞의 problem_b.py 의 값들의 합

# D. 다른폴더에 있는 파일과 비교하기
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

#json과 open을 이용해서 값들을 불러온다. 변수와 알고리즘을 다시 확인하기

# E 다른폴더의 파일과 비교하여 필요한 값들을 뽑기
def dec_movies(movies):
    # 여기에 코드를 작성합니다.         
    movie_name = [] # 영화 제목을 받는 list
    for movie in movies:        
        movie_id =movie['id']    
        month_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        month_list = json.load(month_json)    #12월은 문자열
        if month_list['release_date'][5:7] == '12':  # 해당하는 월을 받기 위해 slicing 사용하기           
            movie_name += [month_list['title']]  #해당하는 영화이름 받아서 추가하기
    return movie_name

# 위의 D와 거의 같고 뽑아내는 값들을 여러개 뽑기