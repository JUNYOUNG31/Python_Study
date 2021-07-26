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