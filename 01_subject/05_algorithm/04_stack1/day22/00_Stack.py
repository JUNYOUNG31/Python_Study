#스택을 만들기 위해서

# 1. 파이썬의 리스트를 이용해서 만들어보자...

stack_list = []

# push
stack_list.append(1)

# peek (당연하게도 공백 검사를 진행한 후 봐야함)
if stack_list:
    stack_list[-1]
    stack_list[len(stack_list)-1]

# pop (공백 검사 후 꺼내야 한다.)
if len(stack_list) > 0:
    stack_list.pop()
    stack_list.pop(-1)
    stack_list.pop(len(stack_list)-1)

#####################################################################

# 일반적인 언어에서 배열을 이용하여 사용한 경우는

stack_arr = [0] * 1000000
top = -1 #마지막 원소를 가리킨다.

# push (가득 차있는지 검사를 한다음 집어넣어야한다)
if len(stack_arr) - 1 > top:
    top += 1
    stack_arr[top] = 1

    # stack_arr[++top]

# peek 공백검사후 확인
if top >= 0:
    stack_arr[top]

# pop 공백검사후 확인
if top >= 0:
    N = stack_arr[top]
    top -= 1

    # stack_arr[top--]









