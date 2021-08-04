#홀수만 담기
#range slicing list 이용해서 1부터 50까지 홀수 구하기
print(list(range(50)[1:50:2]))

#dictionary만들기
#key = '이름' , values = 나이
students = {'박준영': 27,'홍길동': 30,'이순신': 45}

#반복문으로 네모 출력
n = 5
m = 9
i = 0
if i <= m :
    for i in range(1,m + 1):
        print('*'*n)
        i+=1
        
# 조건 표현식
# temp = 36.5
# if temp >= 37.5:
#     print('입실 불가')
# else:
#     print('입실 가능')
temp = 36.5
print('입실 불가') if temp >= 37.5 else print('입실 가능')

# 평균 구하기
scores = [80, 89, 99, 83]
print(sum(scores)/len(scores))