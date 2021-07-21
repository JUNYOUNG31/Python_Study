# 1 built-in 함수
# abs(), max(), min(), sum(), print()

#2. 정중앙 문자
def get_middle_char(i):
    if len(i)%2==0:
        a= i[int(len(i)/2)-1]+i[int(len(i)/2)]
    else:
        a= (i[int(len(i)/2)])
    return print(a)

get_middle_char('ssafy')  #=>a
get_middle_char('coding') #=>di

#3.위치인자와 키워드 인자
def ssafy(name,location='서울'):
    print(f'{name}의 지역은 {location}입니다.')

#(1)
ssafy('이순신')

#(2)
ssafy(location='부산', name='민수')

#(3)
ssafy('춘화', location='대전')

#(4)
# ssafy(name='순재', '부산')

#4. 나의 반환값은
def my_func(a,b):
    c = a + b
    print(c)

result = my_func(5,6)

#5 가변 인자 리스트
def my_avg(*args):
    total = 0
    for i in args:
        total += i
    return total /len(args)

print(my_avg(77, 85, 95, 92, 71, 90))