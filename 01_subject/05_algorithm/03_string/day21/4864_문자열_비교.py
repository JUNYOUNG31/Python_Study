# 문자열 비교

T = int(input())                        # case 수
for tc in range(1, T+1):                # case 반복
    N = str(input())    # 찾을 패턴
    M = str(input())    # 전체 텍스트
    n = len(N)  # 찾을 패턴의 길이
    m = len(M)  # 전체 텍스트 길이
    i = 0
    j = 0
    ans = 0
    while j < n and i < m:
        if M[i] != N[j]:
            i = i - j  # 검색위치 쉬프트
            j = -1
        i = i + 1  # 검색위치를 1칸 푸쉬
        j = j + 1  # 0 으로 만들어서 검색할 처음으로
    if j == n:
        ans = 1
    else:
        ans = 0  # 검색 실패
    print("#{} {}".format(tc, ans))