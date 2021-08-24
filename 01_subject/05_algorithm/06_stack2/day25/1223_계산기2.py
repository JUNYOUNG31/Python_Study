# 계산기2
for tc in range(1, 11):                         # case 10개 반복
    N = int(input())                            # 식의 길이
    exp = input()                               # 식
    stack = [0]                                 # 연산자를 담을 스택
    num = []                                    # 숫자와 연산할 식
                                                # 후위 표기식으로 변경
    for i in exp:                               # 식을 반복해서
        if i == "(":                            # ( 이면
            stack.append(i)                     # stack 에 추가
        elif i == ")":                          # ) 이면
            while stack[-1] != "(":             # 그전에 ( 일때까지
                num.append(stack.pop())         # pop 하고 push 하고
            stack.pop()                         # 날린다
        elif i == "*" or i == "/":              # * 과 / 면
            while stack[-1] == "*" or stack[-1] == "/": # 그전이 * 과 / 일때까지
                num.append(stack.pop())         # pop 하고 push 하고
            stack.append(i)                     # 스택에 추가
        elif i == "+" or i == "-":              # + 와 - 면
            while stack[-1] == "*" or stack[-1] == "/" or stack[-1] == "+" or stack[-1] == "-": # 모든경우에
                num.append(stack.pop())         # pop 하고 push 하고
            stack.append(i)                     # stack 에 추가
        else:
            num.append(int(i))                  # 아니면 식에 숫자 추가
    while len(stack) != 1:                      # 하나라도 남앗다면
        num.append(stack.pop())                 # 식에 pop 하고 push

    stack2 = []                                 # 연산 시작
    for i in num:                               # 후위로 바꾼 식을 반복해서
        if i == '+':                            # + 가 있다면
            A = int(stack2.pop())               # 값 2개를 빼서
            B = int(stack2.pop())
            stack2.append(B + A)                # 더한값을 추가하고
        elif i == '-':                          # - 이 있다면
            A = int(stack.pop())                # 값 2개 빼서
            B = int(stack.pop())
            stack.append(B - A)                 # 빼기
        elif i == '*':                          # * 이 있다면
            A = int(stack2.pop())               # 값 2개 빼서
            B = int(stack2.pop())
            stack2.append(B * A)                # 곱하기
        elif i == '/':                          # / 이 있다면
            A = int(stack.pop())                # 값 2개 빼서
            B = int(stack.pop())
            stack.append(B // A)                # 나누기
        else:
            stack2.append(i)                    # 나머진 추가
    print("#{} {}".format(tc, stack2[0]))       # 연산이 끝나면 0 인덱스만 남아서 출력




# # 계산기2
# for tc in range(1, 11):                     # case 10개 반복
#     N = int(input())                        # 식의 길이
#     exp = input()                           # 식
#     stack = [0]                             # 연산자를 담을 스택
#     num = []                                # 숫자와 연산할 식
#                                             # 후위 표기식으로 변경
#     for i in exp:                           # 식을 반복해서
#         if i == "*":                        # 곱셈이 있고
#             while stack[-1] == "*":         # 그앞에도 곱셉이 있으면
#                 num.append(stack.pop())     # 식에 연산자 추가
#             stack.append(i)                 # 스택에 추가
#         elif i == "+":                      # 더하기 연산자고
#             while stack[-1] == "*" or stack[-1] == "+": # 그앞이 곱하기나 더하기면
#                 num.append(stack.pop())     # 식에 연산자를 추가
#             stack.append(i)                 # 스택에 추가
#         else:
#             num.append(int(i))              # 숫자면 식에 숫자 추가
#     while len(stack) != 1:                  # 스택에 남은게 있다면 식에 추가
#         num.append(stack.pop())
#
#     stack2 = []                             # 연산 시작
#     for i in num:                           # 후위로 바꾼 식을 반복해서
#         if i == '+':                        # + 가 있다면
#             A = int(stack2.pop())           # 값 2개를 빼서
#             B = int(stack2.pop())
#             stack2.append(B + A)            # 더한값을 추가하고
#         elif i == '*':                      # * 이 있다면
#             A = int(stack2.pop())           # 값 2개 빼서
#             B = int(stack2.pop())
#             stack2.append(B * A)            # 곱하기
#         else:
#             stack2.append(i)                # 나머진 추가
#     print("#{} {}".format(tc, stack2[0]))   # 연산이 끝나면 0 인덱스만 남아서 출력