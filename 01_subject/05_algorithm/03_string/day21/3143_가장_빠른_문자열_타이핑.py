# 가장 빠른 문자열 타이핑
T = int(input())                        # case 수
for tc in range(1, T+1):                # case 반복
    A, B = map(str, input().split())    # 전체 텍스트 , 패턴
    a = len(A)                          # 전체 텍스트 길이
    b = len(B)                          # 패턴 길이
    i = 0
    j = 0
    cnt_B = 0
    ans = 0
    while j < b and i < a:
        if A[i] != B[j]:
            i = i - j   # 검색위치 쉬프트
            j = -1
        i = i + 1       # 검색위치를 1칸 푸쉬
        j = j + 1       # 0 으로 만들어서 검색할 처음으로
        if j == b:      #
            cnt_B += 1  # B의 개수
            j = 0
    ans = a - cnt_B*(b-1)
    print("#{} {}".format(tc, ans))



    #############################
    # 가장 빠른 문자열 타이핑
    T = int(input())  # case 수
    for t in range(1, T + 1):  # 반복
        A, B = map(str, input().strip().split())  # 전체 텍스트 , 패턴
        cnt = 0
        idx = 0
        while idx < len(A):  # 전체 길이보다 을때
            if A[idx:idx + len(B)] == B:  # A안에 B가 있으면
                cnt += 1  # cnt 1 증가
                idx += len(B)  # 인덱스만큼 점프
            else:  # 없으면
                cnt += 1  # cnt 1증가
                idx += 1  # 인덱스 1증가 후 반복

        print("#{} {}".format(t, cnt))