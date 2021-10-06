from collections import deque
#상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

T = int(input())                                                    # case 입력
for tc in range(1, T +1):                                           # case 반복
    N, M = map(int, input().split())                                # 지도
    arr = [input() for _ in range(N)]                               # 문자열 입력
    dist = [[987654321] * M for _ in range(N)]
    Q = deque()
    for i in range(N):                                              # 반복해서
        for j in range(M):                                          # 반복해서
            if arr[i][j] == 'W':                                    # W 가 있으면
                Q.append((i, j))                                    # Q 에 추가
                dist[i][j] = 0                                      # 0으로 바꾸기

    while Q:                                                        # Q 반복
        r, c = Q.popleft()                                          # 팝해서
        for i in range(4):                                          # 방향변환
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:              # 범위안에 있다면
                continue                                            # 계속
            if arr[nr][nc] == 'L' and dist[nr][nc] == 987654321:    # L 이고 0이 아니라면
                dist[nr][nc] = dist[r][c] + 1                       # 한칸 전진
                Q.append((nr, nc))
    cnt = 0
    for i in dist:                                                  # 맵을 반복해서
        for j in i:                                                 # 그줄에
            cnt += j                                                # j를 다 더한다
    print("#{} {}".format(tc, cnt))