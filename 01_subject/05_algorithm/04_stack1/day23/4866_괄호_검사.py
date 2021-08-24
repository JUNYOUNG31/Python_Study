# 괄호 검사
def stacks():                                    # 스택 함수 설정
    for i in inputs:                             # input 의 각 원소 확인
        if i == '(' or i == '{':                 # 여는괄호 확인
            stack_list.append(i)                 # 스택 리스트에 추가
        elif i == ')' or i == '}':               # 닫는 괄호 확인
            if len(stack_list) == 0:             # 스랙 리스트가 비었으면
                return 0                         # 0 반환
            else:
                last_stack = stack_list.pop()        # pop 할 원소 확인
            if last_stack == '(' and i == '}':   # 두개가 다르면
                return 0                         # 0 반환
            elif last_stack == '{' and i == ')': # 두개가 다르면
                return 0                         # 0 반환
    if stack_list:                               # 있다면
        return 0                                 # 0 반환
    else:                                        # 없으면
        return 1                                 # 1 반환


T = int(input())                                 # 입력
for tc in range(1, T+1):                         # case 반복
    stack_list = []                              # 스택 리스트
    inputs = input()                             # 입력
    print("#{} {}".format(tc, stacks()))         # 출력