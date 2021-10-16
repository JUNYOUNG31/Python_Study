# 최소 이동 거리
def Prim():
    dist = [98756321] * (V + 1)
    visited = [0] * (V + 1)
    dist[0] = 0
    for _ in range(V):
        min_idx = -1
        min_value = 987654321
        for i in range(V + 1):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]
        visited[min_idx] = True
        for i in range(V + 1):
            if not visited[i] and dist[i] > dist[min_idx] + adj_arr[min_idx][i]:
                dist[i] = dist[min_idx] + adj_arr[min_idx][i]
    return dist[V]


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj_arr = [[987654321] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj_arr[n1][n2] = w
    print("#{} {}".format(tc, Prim()))
