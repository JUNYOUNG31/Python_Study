# 부분집합의 합
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # 12까지의 숫자
list_data = []                                  # 부분집합 배열
n = len(data)                                   # data 의 개수
for i in range(1 << n):                         # n 번 쉬프트
    list_d = []                                 # 각 부분집합의 리스트
    for j in range(n):                          # n 번반복
        if i & (1 << j):                        # 1을 j 번 쉬프트
            list_d.append(data[j])              # 부분집합을 저장
    list_data.append(list_d)                    # 그부분집합을 전부 저장

T = int(input())                                # 케이스 수
for tc in range(1, T+1):
    cnt = 0                                     # 존재하는 부분집합의 수
    N, K = map(int, input().split())            # N 개  K 합
    for d in list_data:                         # 부분집합중
        sum_data = 0
        if len(d) == N:                         # 길이가 N 이고
            for num in d:                       # 그 합이
                sum_data += num
            if sum_data == K:                   # K 이면
                cnt += 1                        # 1 증가

    print('#{} {}'.format(tc, cnt))