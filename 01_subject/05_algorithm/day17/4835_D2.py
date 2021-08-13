# 구간합
T = int(input())
for case in range(T):
    N, M = map(int, input().split())  # N개 M 연속
    a = list(map(int, input().split()))  # N개 숫자

    max_a = 0
    min_a = 123456789
    sum_a = []
    for i in range(N-M+1):
        hap_a = 0
        for j in range(i, M+i):
            hap_a += a[j]
        sum_a.append(hap_a)

    for i in sum_a:
        if max_a < i:
            max_a = i
        if min_a > i:
            min_a = i

    print("#{} {}".format(case + 1, max_a - min_a))
