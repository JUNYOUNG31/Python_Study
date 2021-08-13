# 달팽이 숫자
dr = [0, 1, 0, -1]      # 우하좌상
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    d = 0                                   # 방향
    r = 0                                   # 행좌표
    c = 0                                   # 열좌표
    num = 1                                 # 숫자 입력
    while num <= N**2:                      # 숫자범위
        arr[r][c] = num                     # 처음에는 1
        num += 1                            # 1씩 증가
        nr = r + dr[d]                      # 오른쪽으로 이동
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:   # 벽을 만나지 않으면
            r, c = nr, nc                   # 그방향으로 쭉 이등
        else:                               # 벽을 만나면
            d = (d+1) % 4   # 0 부터 4 까지 반복하기위해서 4로 나눈 나머지
            r += dr[d]                      # 방향 전환 (시계 방향으로)
            c += dc[d]

    print("#{}".format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()
