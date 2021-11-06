import requests
from tmdb import TMDBHelper
from pprint import pprint


def credits(title):
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록과 목록을 출력.
    영화 id검색에 실패할 경우 None 출력.
    """
    tmdb_helper =TMDBHelper('0d9af9ec28d13f9cd2287cb2b89cd8ca') #key 입력    
    movie_id = tmdb_helper.get_movie_id(title)                  # 제목입력해 movie_id 를 가져오기

    # 영화정보 나타내는 /movie/{movie_id}/credits 를 입력하고 한국으로 설정
    url = tmdb_helper.get_request_url(f'/movie/{movie_id}/credits',language='ko')

    data = requests.get(url).json() # requests 를 통해서 data 가져오기
    actor_name = []     # 배우 이름을 저장할 list 변수 
    crew_name = []      # 제작진 이름을 저장할 list 변수 
    result = {}         # 배우와 제작진을 저장할 dict 변수
    try:                # 예외처리를 통해서 검색할수 없을 경우 None 값 반환
        for i in data.get('cast'):
            if i.get('cast_id') < 10:              # cast_id 가 10 보다 작을 경우
                actor_name.append(i.get('name'))   # 이름을 list 에 추가
    except:
        return None
    try:                # 예외처리를 통해서 검색할수 없을 경우 None 값 반환     
        for i in data.get('crew'): 
            if i.get('department') == 'Directing':  # department = Directing 일 경우
                crew_name.append(i.get('name'))     # 이름을 list 에 추가
    except:
        return None
        
    result = {'cast' : actor_name, 'crew' :crew_name}   # 배우와 제작진의 값을 result dict 에 추가
    return result   # dict 값 return

if __name__ == '__main__':
    pprint(credits('기생충'))
    pprint(credits('검색할 수 없는 영화'))