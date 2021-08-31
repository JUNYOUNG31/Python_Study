# 노드의 거리

def bfs(S, G):                                  # 시작과 끝
    Q = []                                      # Q
    visited = [0] * (V+1)                       # 방문 확인
    Q.append(S)                                 # Q에 시작 추가
    visited[S] = 1                              # 방문점시작을 1로 시작
    while Q:
        a = Q.pop(0)
        if a == G:                              # 도착점이면
            return visited[a] - 1
        for i in range(V+1):                    # V까지 돌때
            if visited[i] == 0 and load[a][i]:  # 방문하지 않았고 길이있다면
                Q.append(i)                     # Q 에 추가
                visited[i] = visited[a]+1       # 최솟값 1 씩 추가

    return 0                                    # 오류면 0


T = int(input())                                # 입력
for tc in range(1, T+1):                        # 반복
    V, E = map(int, input().split())            # 노드 갯수 추가
    load = [[0] * (V+1) for _ in range(V+1)]    # 길 추가
    for i in range(E):                          # 반복
        a, b = map(int, input().split())        # 노드들 추가
        load[a][b] = 1                          # 2방향
        load[b][a] = 1
    S, G = map(int, input().split())            # 시작 끝 추가
    print("#{} {}".format(tc, bfs(S, G)))       # 출력
