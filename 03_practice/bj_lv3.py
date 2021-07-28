# 구구단
N = int(input())
for n in range(1,10):
    print(f'{N} * {n} = {N*n}')

# A + B 
T = int(input())
for t in range(1,T+1):
    a, b = map(int, input().split())
    print(a+b)

# N 까지의 합
N = int(input())
hap = 0
for n in range(1,N+1):
    hap += n
print(hap)

# 빠른 A + B
# 이문제의 추가적인 설명은 bj_tip1.py 에서 다룬다.\
import sys
T = sys.stdin.readline() 
total = ''
for t in range(1,int(T)+1):
    a, b = map(int, sys.stdin.readline().split())
    total += (f'{a+b}\n')
print(total)

# N 까지의 숫자 나열
N = int(input())
for n in range(1,N+1):
    print(n)

#N 까지의 숫자 거꾸로 나열
N = int(input())
for n in range(N,0,-1):
    print(n)

# A + B 다른버전
import sys
N = sys.stdin.readline() 
for n in range(1,int(N)+1):
    a, b = map(int, sys.stdin.readline().split())
    print(f'Case #{n}: {a+b}')

# A + B 다른버전
import sys
N = sys.stdin.readline() 
for n in range(1,int(N)+1):
    a, b = map(int, sys.stdin.readline().split())
    print(f'Case #{n}: {a} + {b} = {a+b}')

# 별 찍기
N = int(input())
for i in range(1, N+1):
    print('*'*i)

# 별 찍기 2
N = int(input())
for i in range(1, N+1):
    print(' '*(N-i)+'*'*i)

# x 보다 작은 수
a, b = map(int, input().split())
for A in input().split():
    if int(A) < b :
        print(A,end=' ')