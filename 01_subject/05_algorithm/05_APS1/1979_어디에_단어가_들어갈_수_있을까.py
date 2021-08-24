# 어디에 단어가 들어갈 수 있을까
T = int(input())                                                 # T 입력
for tc in range(1, T + 1):                                       # case 반복
    N, K = map(int, input().split())                             # 크기 N*N 단어의 길이
    stage = [list(map(int, input().split())) for _ in range(N)]  # 맵 설정
    ans = 0                                                      # 정답
    for i in range(N):                                           # 가로 검색
        cnt = 0                                                  # 칸의 길이
        for j in range(N):                                       # 세로 반복
            if stage[i][j] == 1:                                 # 칸이있으면
                cnt += 1                                         # 칸의 길이 + 1
            else:                                                # 칸이끝날때
                if cnt == K:                                     # 만약 칸의 길이랑 같으면
                    ans += 1                                     # 정답 + 1
                cnt = 0                                          # 카운트 초기화
            if j == N-1:                                         # 맨마지막 벽앞
                if cnt == K:                                     # 같으면
                    ans += 1                                     # 정답 + 1
    for i in range(N):                                           # 세로 검색
        cnt = 0
        for j in range(N):
            if stage[j][i] == 1:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
            if j == N - 1:
                if cnt == K:
                    ans += 1
    print("#{} {}".format(tc, ans))
