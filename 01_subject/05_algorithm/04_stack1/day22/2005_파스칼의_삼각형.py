# 파스칼의 삼각형
T = int(input())                # case 수 입력
for tc in range(1, T+1):        # 반복
    N = int(input())            # 삼각형
    pascal = [[0]*i for i in range(1, N+1)]

    pascal[0][0] = 1            # 처음 수 0
    for i in range(1, N):       # 양끝값 1으로 고정
        pascal[i][0] = 1
        pascal[i][-1] = 1
    for i in range(1, N-1):               # i 만큼 반복
        for j in range(len(pascal[i])-1): # j 만큼 반복
            pascal[i+1][j+1] = pascal[i][j] + pascal[i][j+1] # 위의 두개의 핲이 밑에값

    print("#{}".format(tc))               # 출력
    for p in pascal:
        print(*p)