# 회문2
for tc in range(1, 11):                      # case 반복
    T = int(input())                         # case 수
    N = [list(input()) for _ in range(100)]  # 갯수 와 반복구문의 길이
    cnt = 0                                  # 회문의 길이
    for i in range(100):                     # 가로 찾기
        for j in range(100):                 #
            for k in range(99, 0, -1):       # 회문의 길이
                if j + k <= 100:             # 인덱스 100이하
                    for l in range(k // 2):  # 회문찾을 반값
                        if N[i][j + l] != N[i][j + k - 1 - l]:  # 앞뒤가 같지않으면
                            break            # k 증가
                    else:
                        if cnt < k:          # 최대값을 k 로 갱신
                            cnt = k
                            break

    for i in range(100):                     # 세로 찾기
        for j in range(100):                 #
            for k in range(99, 0, -1):       # 회문의 길이
                if j + k <= 100:
                    for l in range(k // 2):
                        if N[j + l][i] != N[j + k - 1 - l][i]:
                            break
                    else:
                        if cnt < k:
                            cnt = k
                            break

    print("#{} {}".format(tc, cnt))  # case 마다 출력
