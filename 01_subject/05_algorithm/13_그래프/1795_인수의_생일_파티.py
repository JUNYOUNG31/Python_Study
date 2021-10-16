# 인수의 생일 파티

def dijkstra(distance, adj):
    visited = [0] * (N + 1)
    distance[x] = 0
    for _ in range(N - 1):
        min_idx = -1
        min_value = 123456789
        for i in range(1, N + 1):
            if not visited[i] and distance[i] < min_value:
                min_idx = i
                min_value = distance[i]
        visited[min_idx] = 1
        for i in range(1, N + 1):
            if not visited[i] and distance[i] > distance[min_idx] + adj[min_idx][i]:
                distance[i] = distance[min_idx] + adj[min_idx][i]


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    adj1 = [[987654321] * (N+1) for _ in range(N+1)]
    adj2 = [[987654321] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        adj1[x][y] = c
        adj2[y][x] = c
    dist1 = [987654321] * (N+1)
    dist2 = [987654321] * (N+1)
    dijkstra(dist1, adj1)
    dijkstra(dist2, adj2)
    max_value = 0
    for i in range(1, N+1):
        if dist1[i] + dist2[i] > max_value:
            max_value = dist1[i] + dist2[i]
    print("#{} {}".format(tc, max_value))