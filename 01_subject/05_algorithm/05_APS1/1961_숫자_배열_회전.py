# 숫자 배열 회전
def trun90(list_N):                                # 함수 선언
    turn_list = [[0] * N for _ in range(N)]        # 빈 2차 배열
    for i in range(N):                             # N 만큼 반복
        for j in range(N):                         # N 만큼 반복
            turn_list[i][j] = list_N[N - 1 - j][i] # 자리 변경 00 => 20 이 된다
    return turn_list                               # 새로 바뀐 배열을 반환


T = int(input())                                   # case 입력
for tc in range(1, T + 1):                         # case 반복
    N = int(input())                               # 크기 입력
    list_N = [input().split() for _ in range(N)]   # 숫자 입력
    list90 = trun90(list_N)                        # 90도 회전
    list180 = trun90(list90)                       # 180도 회전
    list270 = trun90(list180)                      # 270도 회전

    print('#{}'.format(tc))
    for i in range(N):                             # N 만큼 반복
        print(''.join(list90[i]), end=" ")         # 90 1개
        print(''.join(list180[i]), end=" ")        # 180 1개
        print(''.join(list270[i]))                 # 270 1개 씩 출력
