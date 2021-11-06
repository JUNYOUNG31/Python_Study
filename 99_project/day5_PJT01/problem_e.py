import json


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
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))