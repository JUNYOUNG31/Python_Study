# 등산로 조정

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def work(r, c, road, skill):                                       # 1. 현재 위치를 들고 있지 않을때
    global ans                                                     # r,c 좌표, road 길이 skill 공사 유무
    if road > ans:                                                 # 답 갱신
        ans = road
    visited[r][c] = 1                                              # 방문처리
    for i in range(4):                                             # 방향 전환
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:    # a, 현위치보다 낮은곳으로 갈때
            if mountain[r][c] > mountain[nr][nc]:
                work(nr, nc, road + 1, skill)
            elif skill and mountain[r][c] > mountain[nr][nc] - K:  # b, 현위치보다 높거나 같은 곳으로 갈때
                tmp = mountain[nr][nc]                             # 기록
                mountain[nr][nc] = mountain[r][c] - 1
                work(nr, nc, road + 1, 0)                          # 스킬 사용
                mountain[nr][nc] = tmp                             # 원상복귀
    visited[r][c] = 0


T = int(input())                                                   # case 입력
for tc in range(1, T+1):                                           # case 반복
    N, K = map(int, input().split())                               # 지도의 길이, 공사 깊이
    mountain = [list(map(int, input().split())) for _ in range(N)] # 지도 입력
    max_h = 0                                                      # 봉우리의 최대값
    visited = [[0] * N for _ in range(N)]
    ans = 0
    for i in range(N):                                             # max_h 찾기
        for j in range(N):
            if max_h < mountain[i][j]:
                max_h = mountain[i][j]
    for i in range(N):                                             # 최대 봉우리를 찾았다면
        for j in range(N):                                         # work 함수 실행
            if mountain[i][j] == max_h:
                work(i, j, 1, 1)
    print("#{} {}".format(tc, ans))