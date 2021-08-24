#그래프 경로
def dfs(S, G):                                      # 함수 설정
    visited = [0]*(V+1)                             # 방문 경로
    stack = []                                      # 스텍 리스트
    visited[S] = 1                                  # 현재 위치
    while S != G:                                   # 도착지가 아니면 반복
        for w in range(1, V+1):                     # 방문경로
            if ad[S][w] == 1 and visited[w] == 0:
                stack.append(S)                     # 방문 경로 저장
                S = w                               # 새 방문지 이동
                visited[S] = 1
                break
        else:                                        # 다음 정점이 없으면
            if stack:
                S = stack.pop()                      # 지나온 정점이 남아있는 경우
            else:
                break                                # 지나온 정점이 남아있지 않은 경우
    if S == G:
        return 1
    else:
        return 0


T = int(input())                                    # case 입력
for tc in range(1, T+1):                            # case 반복
    V, E = map(int, input().split())                # V 노드 E 간선
    ad = [[0] * (V + 1) for _ in range(V + 1)]      # 리스트 생성
    for _ in range(E):                              # 간선 설정
        n1, n2 = map(int, input().split())          # 방향성
        ad[n1][n2] = 1                              # 1방향
        # ad[n2][n1] = 1                            # 이건 안댐
    S, G = map(int, input().split())                # S 출발 G 도착
    print("#{} {}".format(tc, dfs(S, G)))           # dfs 출발과 도착
