import json
from pprint import pprint


def movie_info(movie, genres):
    # 여기에 코드를 작성합니다.  
    genre_names =[]  #genre의 이름  
    for g_id in genres: # genres의 id
        for m_id in movie['genre_ids']: # movie의 id
            if g_id['id'] == m_id:
                genre_names += [g_id['name']]   

    detail ={
        'id': movie.get('id'),
        'title' : movie['title'],
        'poster_path' : movie.get('poster_path'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_name' : genre_names  # 'genre_ids' 를 'genre_name' 로 변경
    }
    
    return detail


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))