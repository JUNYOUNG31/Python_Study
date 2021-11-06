import requests
from tmdb import TMDBHelper


def popular_count():
    """
    popular 영화목록의 개수 출력.
    """
    tmdb_helper = TMDBHelper('0d9af9ec28d13f9cd2287cb2b89cd8ca')  #나의 key 값 입력
    url = tmdb_helper.get_request_url(region='KR',language='ko')  # region 과 language 를 한국으로 설정
                                      # method='/movie/popular' 는 default 값
    data = requests.get(url).json()   # requests 를 통해서 data 가져오기
    return (len(data.get('results'))) # results의 개수 len 사용

if __name__ == '__main__':
    print(popular_count())
