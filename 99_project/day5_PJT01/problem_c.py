import json
from pprint import pprint


def movie_info(movies, genres):
    #여기에 코드를 작성합니다.  
    movie_all =[]  # 모든 movie를 불러오는 list
    for movie_name in movies:  # 영화 목록 가져오는 반복문
        genre_names =[]  
        for g_id in genres:                        
            for m_id in movie_name['genre_ids']:
                if g_id['id'] == m_id:
                    genre_names += [g_id['name']]   

        detail ={
        'id': movie_name.get('id'),
        'title' : movie_name['title'],
        'poster_path' : movie_name.get('poster_path'),
        'vote_average' : movie_name.get('vote_average'),
        'overview' : movie_name.get('overview'),
        'genre_name' : genre_names    
        }
        movie_all += [detail]  # 앞의 problem_b.py 의 값들을 더해준다
    
    return movie_all
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))