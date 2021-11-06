import json
from pprint import pprint


def movie_info(movie):    
    # 여기에 코드를 작성합니다.  
    # detail = dictionary에 입력할 값들 
    detail ={
        'id': movie.get('id'),
        'title' : movie['title'],
        'poster_path' : movie.get('poster_path'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_ids' : movie.get('genre_ids'),
        'name' : movie.get('name') #get 은 에러가나지않고 none 반환
      # 'name' : movie['name']  에러가 난다. 
    }
    return detail 

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))