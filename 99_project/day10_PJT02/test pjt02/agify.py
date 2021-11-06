import requests

#요청을 보낼 URL
url = 'https://api.agify.io?name=michael'

#응답 json str을 dict 로 파싱해서 response에 저장
response = requests.get(url).json()

print(response['age'])
print(response)