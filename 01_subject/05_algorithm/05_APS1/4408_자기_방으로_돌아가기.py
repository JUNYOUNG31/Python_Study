# 자기 방으로 돌아가기
def div(num):                       # 함수 선언
    return (int(num) + 1) // 2


def max_s(road):
    s = road[0]
    for i in road:
        if s < i:
            s = i
    return s


T = int(input())                    # case 수
for tc in range(1, T + 1):          # case 반복
    N = int(input())                # 사람의 수
    students = [list(map(div, input().split())) for _ in range(N)]

    road = [0] * 201

    for i in range(N):
        if students[i][0] > students[i][1]:
            students[i][0], students[i][1] = students[i][1], students[i][0]

        for j in range(students[i][0], students[i][1] + 1):
            road[j] += 1

    print("#{} {}".format(tc, max_s(road)))