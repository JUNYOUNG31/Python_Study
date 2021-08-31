# 미로1
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def BFS(r, c):                                                     # bfs
    Q = [(r, c)]                                                   # 시작점의 위치 Q
    visited[r][c] = 1                                              # 시작점은 1
    while Q:
        curr_r, curr_c = Q.pop(0)                                  # 위치
        visited[curr_r][curr_c] = 1
        for i in range(4):                                         # 상하좌우
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]
            if nr < 0 or nr >= 16 or nc < 0 or nc >= 16: continue  # 벽이아니라면
            if arr[nr][nc] == 0 and visited[nr][nc] == 0:          # '0'이고 방문하지 않았다면
                Q.append((nr, nc))                                 # 추가
            elif arr[nr][nc] == 3:                                 # 3이 도착지
                return 1
    return 0


for tc in range(1, 11):                                     # case 반복
    T = int(input())                                        # case 입력
    arr = [list(map(int, input())) for _ in range(16)]      # 지도
    visited = [[0] * 16 for _ in range(16)]                 # 방문 기록
    for i in range(16):                                     # 시장위치찾기
        for j in range(16):
            if arr[i][j] == 2:                              # 2일때
                r = i                                       # 행
                c = j                                       # 열

    print("#{} {}".format(tc, BFS(r, c)))                   # 출력