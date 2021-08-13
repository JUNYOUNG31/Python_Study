# Ladder1
dr = [0, 0, -1]  # 우 좌 상
dc = [1, -1, 0]

for tc in range(1, 11):
    T = int(input())
    Ladder = [list(map(int, input().split())) for _ in range(100)]
    d = 0
    r = 0
    c = 0
    ans_i = 0                      # 출발 지점
    for i in range(100):           # 100 번 반복하는데  거꾸로 시작
        if Ladder[99][i] == 2:     # 마지막행  i 번째가 2 이라면
            r = 99                 # 행좌표 99
            c = i                  # 열좌표
            now = 0                # 현재 상태
    while r != 0:                  # 행이 100이 될때까지 반복
        if 0 <= r+dr[0] < 100 and 0 <= c+dc[0] < 100:        # 오른쪽으로 움직일때 벽을 만나지 않으면서
            if Ladder[r+dr[0]][c+dc[0]] == 1 and now != 1:   # 오른쪽옆이 1이고 현재상태가 1(왼쪽으로움직이는게 아닐때)
                r, c = r+dr[0], c+dc[0]                      # 그방향으로 진행하고
                now = 2                                      # 현재상태 2
                continue
        if 0 <= r+dr[1] < 100 and 0 <= c+dc[1] < 100:        # 왼쪽으로 움직일때 벽을 만나지 않으면서
            if Ladder[r+dr[1]][c+dc[1]] == 1 and now != 2:   # 왼쪽옆이 1이고 현재상태가 2(오른쪽으로 움직이는게 아닐때)
                r, c = r+dr[1], c+dc[1]                      # 그방향으로 진행하고
                now = 1                                      # 현재상태 1
                continue
        r, c = r + dr[2], c + dc[2]                          # 둘다 아니면 위로 한칸
        now = 0                                              # 현재상태 0

    ans_i = c                                                # 현재출발 지점
    print("#{} {}".format(tc, ans_i))
