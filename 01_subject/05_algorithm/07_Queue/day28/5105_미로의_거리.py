# 미로의 거리
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def BFS(r, c):                                                  # bfs
    Q = [(r, c)]                                                # 시작점의 위치 Q
    visited[r][c] = 1                                           # 시작점은 1
    while Q:
        curr_r, curr_c = Q.pop(0)                               # 위치
        for i in range(4):                                      # 상하좌우
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue # 벽이아니라면
            if arr[nr][nc] == '0' and visited[nr][nc] == 0:     # '0'이고 방문하지 않았다면
                Q.append((nr, nc))                              # 추가
                visited[nr][nc] = visited[curr_r][curr_c] + 1   # 방문에 +1
            elif arr[nr][nc] == '3':                            # 3이 도착지
                return visited[curr_r][curr_c] - 1              # 현재 값에서 시작값 1 빼기

    return 0


T = int(input())                            # case 입력
for tc in range(1, T+1):                    # case 반복
    N = int(input())                        # 사각형
    arr = [list(input()) for _ in range(N)] # 지도
    visited = [[0] * N for _ in range(N)]   # 방문 기록록
    for i in range(N):                      # 시장위치찾기
       for j in range(N):
            if arr[i][j] == '2':            # 2일때
                r = i                       # 행
                c = j                       # 열

    print("#{} {}".format(tc, BFS(r, c)))   # 출력