# 색칠하기
T = int(input())
for tc in range(T):
    N = int(input())  # N 개
    box = [[0] * 10 for i in range(10)]  # 2차원 배열 만들기
    count = 0  # 겹친 종이수
    for n in range(N):  # N번 반복
        c1, r1, c2, r2, color = map(int, input().split())  # 좌표 (r1,c1) (r2,c2) 2개
        for c in range(c1 - 1, c2):  # x 좌표
            for r in range(r1 - 1, r2):  # y 좌표
                box[c][r] += color  # 해당하는 좌표 색 추가

    for c in range(len(box)):  # 행우선 순회
        for r in range(len(box[0])):
            if box[c][r] == 3:  # 겹친수가 3 이면 보라색
                count += 1  # 1씩 추가

    print('#{} {}'.format(tc+1, count))
