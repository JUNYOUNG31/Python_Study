def dfs(s, V):
    visited = [0]*(V+1)
    stack = []
    i = s  # 현재 방문한 정점 i
    visited[i] = 1
    while i!=0: #True:
        for w in range(1, V+1):
            if adj[i][w] == 1 and visited[w]==0:
                stack.append(i) # 방문 경로 저장
                i = w           # 새 방문지 이동
                visited[w] = 1
                break
        else:           # 다음 정점이 없으면
            if stack:
                i = stack.pop()   # 지나온 정점이 남아있는 경우
            else:
                i = 0             # 지나온 정점이 남아있지 않은 경우
                # break
    return


#          A  B  C  D  E  F  G
adj = [[0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 0, 0], # A
       [0, 1, 0, 0, 1, 1, 0, 0], # B
       [0, 1, 0, 0, 0, 1, 0, 0], # C
       [0, 0, 1, 0, 0, 0, 1, 0], # D
       [0, 0, 1, 1, 0, 0, 1, 0], # E
       [0, 0, 0, 0, 1, 1, 0, 1], # F
       [0, 0, 0, 0, 0, 0, 1, 0]] # G
node = ['', 'A','B','C','D','E','F','G']
'''
7 8
1 2
1 3
...
'''
V, E = map(int, input().split())
ad = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
   n1, n2 = map(int, input().split())
   ad[n1][n2] = 1
   ad[n2][n1] = 1

dfs(1, 7)