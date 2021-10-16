## ㅋㅋ 실은 5249번 문제임

def Prim():
    dist = [98756321] * (V + 1)
    visited = [0] * (V + 1)

    dist[0] = 0

    #어차피 마지막 정점은 돌지 않아도 되니까
    # 정점의 개수 -1 만큼 만 돌면되는데 여기서는 조금 예외
    for _ in range(V):
        min_idx = -1
        min_value = 987654321

        # 최소 인덱스를 찾자.
        for i in range(V + 1):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]

        visited[min_idx] = True
        # 갱신할수있는 친구덜 전부 갱신하자고~
        for i in range(V + 1):
            if not visited[i] and adj_arr[min_idx][i] < dist[i]:
                dist[i] = adj_arr[min_idx][i]

    return sum(dist)


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())  # V : 마지막 정점의 번호, E 간선의 개수

    adj_arr = [[987654321] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj_arr[n1][n2] = adj_arr[n2][n1] = w

    print("#{} {}".format(tc, Prim()))
