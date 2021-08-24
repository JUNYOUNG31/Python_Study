# GNS
List_number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())                            # 입력 수
for tc in range(1, T+1):                    # case 반복
    t, len_N = map(str, input().split())    # #case 번호와 길이 를 str 로 받는다
    N = list(map(str, input().split()))     # 문자로된 숫자를 str로 리스트화
    ans = []                                # 답 리스트
    for i in range(10):                     # 위의 정렬된 숫자 중에서
        for j in N:                         # N 을 반복시켜서
            if List_number[i] == j:         # 같이 같다면
                ans.append(List_number[i])  # 리스트에 추가
    print(t)                                # 케이스 출력하고
    print(*ans)                             # 답 리스트 출력
