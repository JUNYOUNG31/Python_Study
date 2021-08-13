# 특별한 정렬
T = int(input())
for tc in range(1, T+1):
    N = int(input())                                # 숫자 개수
    a = list(map(int, input().split()))             # 숫자 입력
    ans = []
    for i in range(10):                             # 10개만 출력
        if i % 2:                                   # 홀수 일때
            min_idx = i                             # 최소값으로 정렬
            for j in range(i + 1, N):
                if a[min_idx] > a[j]:
                    min_idx = j
            a[i], a[min_idx] = a[min_idx], a[i]
            ans.append(a[i])
        else:                                       # 짝수면
            max_idx = i                             # 최대값으로 정렬
            for k in range(i + 1, N):
                if a[max_idx] < a[k]:
                    max_idx = k
            a[i], a[max_idx] = a[max_idx], a[i]
            ans.append(a[i])
    print("#{}".format(tc), end=' ')
    print(*ans)

