import requests
from tmdb import TMDBHelper
from pprint import pprint


def vote_average_movies():
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    
    tmdb_helper = TMDBHelper('0d9af9ec28d13f9cd2287cb2b89cd8ca')  #나의 key 값 입력
    url = tmdb_helper.get_request_url(region='KR',language='ko')  # region 과 language 를 한국으로 설정
                                       # method='/movie/popular' 는 default 값
    data = requests.get(url).json()    # requests 를 통해서 data 가져오기
    high_vote_movie = []               # 평점높은 movie 값의 list 변수
    for i in data.get('results'):      # results 중에서
        if i.get('vote_average') >= 8: # 평점이 8이상인 영화가 있다면
            high_vote_movie.append(i)  # 새로운 리스트에 추가해라
    
    return high_vote_movie             # 추가된 movie 값 return

if __name__ == '__main__':
    pprint(vote_average_movies())