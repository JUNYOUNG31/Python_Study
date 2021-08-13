# 선택 정렬
T = int(input())                               # case 수
for tc in range(1, T + 1):
    N = int(input())                           # 숫자 수
    list_N = list(map(int, input().split()))   # N 값

    for i in range(N-1):                       # 마지막 값 빼고
        min_idx = i                            # 제일 작은 인덱스 변수
        for j in range(i+1, N):                # +1 부터 끝까지 탐색
            if list_N[min_idx] > list_N[j]:    # j번째 값이 더 작으면
                min_idx = j                    # 인덱스 변경
        list_N[i], list_N[min_idx] = list_N[min_idx], list_N[i] # 위치 바꾸기

    print('#{}'.format(tc), end=' ')
    print(*list_N)