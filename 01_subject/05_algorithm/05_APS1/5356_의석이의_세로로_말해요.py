# 의석이의 세로로 말해요
T = int(input())                              # case 수
for tc in range(1, T + 1):                    # case 반복
    word = [list(input()) for _ in range(5)]  # 5줄 입력
    ans = ''                                  # 정답
    for i in range(15):                       # 가로
        for j in range(5):                    # 세로
            if i < len(word[j]):              # 가로 인덱스가 문자열 안에 있으면
                ans += word[j][i]             # 정답에 추가
    print("#{} {}".format(tc, ans))