import requests
from tmdb import TMDBHelper
from pprint import pprint


def movie_review(title):
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 리뷰를 가져오는 함수
    """
    tmdb_helper =TMDBHelper('0d9af9ec28d13f9cd2287cb2b89cd8ca') #key 입력
    movie_id = tmdb_helper.get_movie_id(title)                  # 제목입력해 movie_id 를 가져오기

    # 영화의 리뷰 나타내는 /movie/{movie_id}/reviews 를 입력  (한글 리뷰는 없다... ㅠㅠ)
    url = tmdb_helper.get_request_url(f'/movie/{movie_id}/reviews')
    
    data = requests.get(url).json()                 # requests 를 통해서 data 가져오기    
    review_list = []                                # 리뷰를 저장할 list 변수
    try: # 예외처리를 통해서 검색할수 없을 경우 None 값 반환
        for i in data.get('results'):      
            review_list.append(i.get('content')) #review 내용 추가           
    except:
        return None
    
    return review_list                               # review 내용 return

if __name__ == '__main__':
    pprint(movie_review('Black Widow'))              # 블랙 위도우
    pprint(movie_review('Snowpiercer'))              # 설국열차
    pprint(movie_review('The Shawshank Redemption')) # 쇼생크 탈출