# 숫자를 정렬하자
import sys
sys.stdin = open("1966_input.txt", "r")

T = int(input())
for case in range(T):
    N = int(input())
    num = list(map(int, input().split()))
    ans = 0
    for i in range(len(num) - 1, 0, -1):
        for j in range(0, i):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    ans = ' '.join(map(str, num))

    print(f'#{case + 1} {ans}')