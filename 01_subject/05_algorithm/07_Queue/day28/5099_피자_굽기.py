# 피자 굽기
T = int(input())                                   # case 입력
for tc in range(1, T+1):                           # case 반복
    N, M = list(map(int, input().split()))         # 화덕수 피자수
    Ci = list(map(int, input().split()))           # 피자의 치즈의 양
    Q = []                                         # Q = 오븐 리스트
    pizza_list = []                                # 피자번호와 치즈양 리스트
    for i in range(M):                             # 피자번호와 치즈양 추가
        pizza_list.append([Ci[i], i])
    pizza_list_reverse = pizza_list[::-1]          # pop하기 위해서 거꾸로 된 리스트 생성
    for i in range(N):                             # 화덕에 뒤에서 부터 추가하므로 0번 부터 들어간다
        Q.append(pizza_list_reverse.pop())
    while len(Q) != 1:                             # 반복
        Q[0][0] //= 2                              # 치즈의 양을 반으로 나누기
        if Q[0][0] == 0:                           # 만약 0 이라면
            Q.pop(0)                               # 첫번째 피자는 뺀다
            if len(pizza_list_reverse) != 0:       # 그리고 피자가 남아있다면
                Q.append(pizza_list_reverse.pop()) # 피자를 오븐에 넣기
        else:
            Q.append(Q.pop(0))                     # 치즈가 남아잇으면 맨뒤로 가기
    print("#{} {}".format(tc, Q[0][1]+1))          # index + 1  피자번호