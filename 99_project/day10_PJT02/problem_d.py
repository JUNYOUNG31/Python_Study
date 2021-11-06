import requests
from tmdb import TMDBHelper
from pprint import pprint


def recommendation(title):
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록을 출력.
    추천 영화가 없을 경우 [] 출력.
    영화 id검색에 실패할 경우 None 출력.
    """
    tmdb_helper =TMDBHelper('0d9af9ec28d13f9cd2287cb2b89cd8ca') #key 입력
    movie_id = tmdb_helper.get_movie_id(title)                  # 제목입력해 movie_id 를 가져오기

    # 추천영화를 나타내는 /movie/{movie_id}/recommendations 를 입력하고 한국으로 설정
    url = tmdb_helper.get_request_url(f'/movie/{movie_id}/recommendations', region='KR',language='ko')
    
    data = requests.get(url).json()               # requests 를 통해서 data 가져오기
    movie_name = []                               # 이름을 저장할 list 변수 
    try:                                          # 예외처리를 통해서 검색할수 없을 경우 None 값 반환
        for i in data.get('results'):             # 값이 없을경우 반환하기위해 get 사용       
                movie_name.append(i.get('title')) #title값 추가
    except:
        return None
    return movie_name                             # 추가된 title 값의 list return


if __name__ == '__main__':
    pprint(recommendation('기생충'))
    pprint(recommendation('그래비티'))
    pprint(recommendation('검색할 수 없는 영화'))
