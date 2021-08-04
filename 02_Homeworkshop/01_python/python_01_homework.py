#1. Pythone 예약어
# keyword.kwlist

#2. 실수 비교
import math
num1 = 0.1 * 3
num2 = 0.3
print(math.isclose(num1, num2))

#3. 이스케이프 시퀀스
print('(1) 줄 바꿈\n(2) 탭,\t (3)백슬래시\\')

#4. String Interpolation
name ='철수'
print(f'안녕, {name}야')

#5. 형 변환
print(str(1))
print(int('30'))
print(int(5))
print(bool('50'))
# print(int('3.5'))

#6. 네모 출력
n = 5
m = 9
print((('*'*n)+'\n')*m)

for i in range(m) :
    for j in range(n) :
        print('*', end = '')
    print()

#7. 이스케이프 시퀀스 응용
print('"파일은 C:\\Winsdows\\Users\\내문서\\Python에 저장이 되었습니다."\n나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'')

#8. 근의 공식
a = float(input())
b = float(input())
c = float(input())
x = b**2.0 - 4.0 * a * c
ans1 = ((-b + x**0.5) / 2.0 * a )
ans2 = ((-b - x**0.5) / 2.0 * a )
print(f'{a}x^2+{b}x+{c}')
print(ans1)
print(ans2)