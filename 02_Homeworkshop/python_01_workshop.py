# 정수 세로 출력
number = int(input())

for num in range( 1, number + 1):
    print(num)

# 정수 거꾸로 출력
number = int(input())

for num in range( number ,-1,-1):
    print(num)

#N 줄 덧셈
number=int(input())
sumi = 0
for i in range(1, number+1):
        sumi += i
print(sumi)