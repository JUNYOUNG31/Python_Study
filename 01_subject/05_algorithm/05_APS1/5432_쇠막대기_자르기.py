# 쇠막대기 자르기
T = int(input())                        # case
for tc in range(1, T + 1):              # case 반복
    sticks = input()                    # 레이저와 막대기
    stick = 0                           # 막대기 개수
    ans = 0                             # 총막대기 수
    for i in range(len(sticks)):        # 길이 만큼 반복
        if sticks[i] == '(':            # 괄호가 열리고
            if sticks[i + 1] == ')':    # 레이저 일때
                ans += stick            # 막대기수만큼 총 막대수 증가
            else:                       # 레이저가 아니면
                stick += 1              # 막대기 수 + 1
                ans += 1                # 총 막대기 수 + 1
        else:
            if sticks[i - 1] == ')':    # ) ) 면 막대가 하나 줄어듬
                stick -= 1              # 막대기 수 -1

    print('#{} {}'.format(tc, ans))