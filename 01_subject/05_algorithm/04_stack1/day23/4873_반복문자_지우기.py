# 반복문자 지우기
T = int(input())                                # case 수
for tc in range(1, T+1):                        # case 반복
    str1 = input()                              # 문자열
    stack_list = []                             # 스택 리스트
    for i in range(len(str1)):                  # 문자길이만큼 반복
        if not stack_list:                      # 스택 리스트가 비어있다면
            stack_list.append(str1[i])          # 문자를 추가하고
        else:                                   # 없다면
            if stack_list[-1] == str1[i]:       # 스택리스트의 마지막 값이 문자열 i 와 같다면
                stack_list.pop()                # 스택리스트에서 삭제하고
            else:                               # 같지않다면
                stack_list.append(str1[i])      # 문자 i 를 스택리스트에 추가한다.

    print("#{} {}".format(tc, len(stack_list)))