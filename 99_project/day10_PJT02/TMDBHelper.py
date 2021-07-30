import requests

#프로젝트에 사용할 중복적으로 사용될 값들을 함수로 만들어본다

class TMDBHelper:    

    def __init__(self,api_key=None):
        self.api_key = api_key

    def get_request_url(self, method='/movie/popular',**kwargs):
        base_url = 'https://api.themoviedb.org/3'
        request_url = base_url + method
        request_url += f'?api_key={self.api_key}'

        for k, v in kwargs.items():
            request_url += f'&{k}={v}'
        return request_url
    
    # 제목으로 영화 검색 후, 검색결과에서 id를 return
    def get_movie_id(self, title):
        request_url = self.get_request_url('/search/movie',query=title,region='KR',language='ko')
        #검색 결과 dict
        data = requests.get(request_url).json()

        results = data.get('result') # key 에러방지용 get
        if results: #비어 있는 리스트라면
            movie_id = results[0]['id']
            return movie_id
        else:
            return None
       

tmdb_helper = TMDBHelper('0d9af9ec28d13f9cd2287cb2b89cd8ca')
tmdb_helper.get_request_url(language='ko',region='KR')
print(tmdb_helper.get_movie_id('기생충'))
print(tmdb_helper.get_movie_id('충생기'))






# problem_d.py

th =TMDBHelper('key')
movie_id = th.get_movie_id(title)

# url = th.get_request_url(f 스트링 써서 id )

requests.get(url)

# problem_a.py

tmdb_helper = TMDBHelper('key')
url = tmdb_helper.get_request_url(region='KR',language='ko')

data = requests.get(url).json()

#이 밑으로가 답이므로 채워넣기
# popular_movies = data[]

