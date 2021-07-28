# 두수 비교하기
a, b = map(int, input().split())
if a > b :
    print('>')
elif a < b :
    print('<')
elif a == b :
    print('==')

# 점수에 따른 학점 분배
a = int(input())
if 90 <= a :
    print('A')
elif 80 <= a :
    print('B')
elif 70 <= a :
    print('C')
elif 60 <= a :
    print('D')
else:
    print('F')

# 윤년
a = int(input())
if a % 4 == 0:
    if a % 100 != 0 :
        print(1)
    elif a % 400 == 0:
        print(1)
    else:
        print(0)
else:
    print(0)

# 사분면 고르기
x = int(input())
y = int(input())
if x > 0 and y > 0 :
    print(1)
elif x < 0 and y > 0 :
    print(2)
elif x < 0 and y < 0 :
    print(3)
elif x > 0 and y < 0 :
    print(4)

# 시간 알리기
h, m = map(int, input().split())
if 0 < h < 24 and 0 <= m < 45 :
    h = h - 1   
    m = m + 15    
elif 0 <= h < 24 and 45 <= m < 60 :
    h = h
    m = m - 45
elif h == 0 and 0 <= m < 45 :
    h = 23
    m = m + 15
print(h,m)