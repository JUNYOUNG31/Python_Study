# 길찾기
def dfs(v):                                   # 재귀함수
    visited[v] = 1                            # 방문한곳으로 1
    for w in range(100):                      # 100번 반복
        if adj[v][w] == 1 and not visited[w]: # 값이 있고 방문하지않았다면
            dfs(w)                            # 재귀


for tc in range(10):                          # 10번 반복
    T, E = map(int, input().split())          # case 수 와 길의 수
    list_E = list(map(int, input().split()))  # 길의 리스트
    adj = [[-1] * 100 for _ in range(100)]     # 행렬 100 100
    visited = [0] * 100                       # 방문 스택
    for i in range(E):                        # E 만큼 반복
        adj[list_E[2*i]][list_E[2*i + 1]] = 1 # 1, 2, 3, 4 => 1, 3 시작 2,4 끝이니깐 점프해서 길 등록

    dfs(0)                                    # 0 부터 시작

    print("#{} {}".format(T, visited[99]))    # 마지막에 길이있으면 1이 출력