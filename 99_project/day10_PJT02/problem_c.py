import requests
from tmdb import TMDBHelper
from pprint import pprint


def ranking():
    """
    popular 영화목록을 정렬하여 평점순으로 5개 출력.
    """
    
    tmdb_helper = TMDBHelper('0d9af9ec28d13f9cd2287cb2b89cd8ca')  #나의 key 값 입력
    url = tmdb_helper.get_request_url(region='KR',language='ko')  # region 과 language 를 한국으로 설정
                                      # method='/movie/popular' 는 default 값

    data = requests.get(url).json()   # requests 를 통해서 data 가져오기
    sort_vote_movie = []              # 정렬할 movie list 변수
    sort_vote_movie = sorted(data.get('results'), key=lambda k: k['vote_average'],reverse=True)
                      # 정렬하는데(정렬할 리스트, key는 한번사용할 함수 k: k의 평점, 오름차순으로)
    return sort_vote_movie[0:5]       # 5개까지만 출력하는 slice 이용
    
if __name__ == '__main__':
    pprint(ranking())

