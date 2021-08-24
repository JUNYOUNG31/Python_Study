# Forth
T = int(input())
for tc in range(1, T + 1):
    exp = input().split()
    stack = []
    for i in exp:                            # 반복
        ans = 0                              # 답 변수
        try:                                 # 예외 처리
            if i == '.':                     # . 면
                if len(stack) != 1:          # stack 수가 1이아니면 연산이 오류
                    ans = 'error'            # error
                    break                    # 멈춰
                ans = stack.pop()            # 아니면 답에 추가
                break
            elif i == '+':                   # + 가 있다면
                A = int(stack.pop())         # 값 2개를 빼서
                B = int(stack.pop())
                stack.append(B + A)          # 더한값을 추가하고
            elif i == '-':                   # - 이 있다면
                A = int(stack.pop())         # 값 2개 빼서
                B = int(stack.pop())
                stack.append(B - A)          # 빼기
            elif i == '*':                   # * 이 있다면
                A = int(stack.pop())         # 값 2개 빼서
                B = int(stack.pop())
                stack.append(B * A)          # 곱하기
            elif i == '/':                   # / 이 있다면
                A = int(stack.pop())         # 값 2개 빼서
                B = int(stack.pop())
                stack.append(B // A)         # 나누기
            else:
                stack.append(i)              # 나머진 추가
        except:
            ans = 'error'

    print("#{} {}".format(tc, ans)) # 연산이 끝나면 0 인덱스만 남아서 출력

