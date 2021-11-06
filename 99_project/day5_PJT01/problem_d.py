import json


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
        
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))