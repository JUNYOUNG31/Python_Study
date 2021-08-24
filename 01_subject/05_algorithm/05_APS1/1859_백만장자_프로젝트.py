# 백만장자 프로젝트
T = int(input())                              # case 수
for tc in range(1, T+1):                      # case 반복
    N = int(input())                          # 개수 입력
    price = list(map(int, input().split()))   # 일별 값
    ans = 0                                   # 이득의 합

    last_p = price[-1]                        # 마지막날의 값
    for i in range(N-1, -1, -1):              # 뒤에서부터 큰값 찾기
        if price[i] < last_p:                 # 마지막날 값이 더크면
            ans += last_p-price[i]            # 이익들의 합
        else:                                 # 마지막날의 값이 작으면
            last_p = price[i]                 # 이전날로 갱신해준다

    print('#{} {}'.format(tc, ans))