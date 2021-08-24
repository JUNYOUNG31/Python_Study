# 회문
T = int(input())                        # case 수
for tc in range(1, T+1):                # case 반복
    N, M = map(int, input().split())    # 갯수 와 반복구문의 길이
    list_N = []                         # N의 집합리스트
    ans = ''                            # 정답
    for _ in range(N):                  # 리스트에 N 들을 추가
        A = list(input())
        list_N.append(A)                # 2차원 배열

    for i in range(N):                  # 가로찾기
        for j in range(N-M+1):          # M 만큼
            for k in range(M//2):       # 회문이니깐 반만 검색
                if list_N[i][j+k] != list_N[i][j-1+M-k]:
                    break               # 없으면 세로찾기로 가기
            else:
                for l in range(M):      # 있다면 M의 길이만큼
                    ans +=(list_N[i][j+l]) # 출력
                break

    for i in range(N):                  # 세로찾기
        for j in range(N-M+1):          # M만큼
            for k in range(M//2):       # 회문이니깐 반만 검색
                if list_N[j+k][i] != list_N[j-1+M-k][i]:
                    break               # 없으면 종료
            else:
                for l in range(M):      # M 의 길이만큼
                    ans += (list_N[j+l][i]) # 답에 저장
                break

    print("#{} {}".format(tc, ans))     # case 마다 출력