# sum
for tc in range(10):        # 10회 반복
    T = int(input())        # case 번호
    data = [list(map(int, input().split())) for _ in range(100)] # 데이터 입력
    max_i = 0               # 가로의 max 값
    max_j = 0               # 세로의 max 값
    max_k = 0               # 대각선의 max 값
    max_l = 0               # 역슬레쉬 max 값
    ans = 0                 # 정답
    for i in range(len(data)):        # 행 우선 순회
        sum_i = 0                     # 합 변수
        for j in range(len(data[i])):
            sum_i += data[i][j]       # 가로의 합을 저장하고
        if max_i < sum_i:             # 그중 최대값 반환
            max_i = sum_i

    for j in range(len(data[0])):     # 열 우선 순회
        sum_j = 0                     # 합 변수
        for i in range(len(data)):
            sum_j += data[i][j]       # 세로의 합을 저장하고
        if max_j < sum_j:             # 그중 최대값 반환
            max_j = sum_j

    for i in range(len(data)):        # 대각선 y = x 축
        for j in range(len(data[i])):
            if i == j:                # y = x 일때
                max_k += data[i][j]   # 모든값의 합

    for i in range(len(data)):        # 대각선 y = -x 축
        for j in range(len(data[i])):
            if i+j == 99:             # 두합이 99일때
                max_l += data[i][j]   # 모든값의 합

    list_max = [max_i, max_j, max_k, max_l]     # 각 max 값을 리스트화
    for a in list_max:                          # 그 중에서
        if ans < a:                             # 최대값 반환
            ans = a
    print("#{} {}".format(tc+1, ans))