# 최소합

# 그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.
# 맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면
# 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.

dr = [0, 1]  # 오른쪽  아래
dc = [1, 0]

def dfs(r, c, hap):                        # dfs
    global ans                             # 답 갱신
    if r == N-1 and c == N-1:              # 마지막값에 도착하면
        hap += pan[r][c]                   # 값 더해주고
        if hap < ans:                      # 이게 이전 갱신값보다 작으면
            ans = hap                      # 갱신하고
            return                         # 멈춰
    for i in range(2):                     # 방향 2개 반복
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:  # 방문안했고
            visited[nr][nc] = 1                                   # 방문처리하고
            dfs(nr, nc, hap + pan[r][c])                          # dfs 돌고
            visited[nr][nc] = 0                                   # 다시 초기화 해주고


T = int(input())                                                  # case 수
for tc in range(1, T+1):                                          # case 반복
    N = int(input())                                              # pan 크기
    pan = [list(map(int, input().split())) for _ in range(N)]     # 수 입력
    visited = [[0]*N for _ in range(N)]                           # 방문 처리
    ans = 123456                                                  # 작은걸로 갱신해야하니깐 큰걸로 설정
    dfs(0, 0, 0)                                                  # dfs 돌리고
    print("#{} {}".format(tc, ans))