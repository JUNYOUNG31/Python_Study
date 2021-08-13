arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

r = 0
c = 1
N = 3

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]

    # 내가 범위 안에 들어와 있을때 아래의 코드를 실행
    # if 0 <= nr < N and 0 <= nc < N:
    #     # print(arr[nr][nc], end=" ")
    #     if arr[nr][nc] == 2:
    #         print("오 2 있네")

    # 첫번째 (에러 안남)
    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 2:
        print("오 2 있네")

    # 두번째 (에러 날수도...)
    if arr[nr][nc] == 2 and 0 <= nr < N and 0 <= nc < N:
        print("오 2 있네")

    # 범위 안에 들어오지 않았다면 그냥 다음 차례로 넘기기
    # if nr < 0 or nr >= N or nc < 0 or nc >= N:
    #     continue
    # print(arr[nr][nc], end=" ")
    #
    # if arr[nr][nc] == 2:
    #     print("오 2 있네")


def my_max(a, b):
    if a > b:
        return a
    else:
        return b
