# 그룹 나누기
def bfs(st):
    Q = [st]
    team[st] = 1
    while Q:
        p = Q.pop(0)
        for i in range(1,  N+1):
            if not team[i] and adj_arr[p][i]:
                team[i] = 1
                Q.append(i)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    edges = list(map(int, input().split()))
    adj_arr = [[0]*(N+1) for _ in range(N+1)]
    for i in range(M):
        person1 = edges[i*2]
        person2 = edges[i*2+1]
        adj_arr[person1][person2] = adj_arr[person2][person1] = 1
    ans = 0
    team = [0] * (N+1)
    for i in range(1, N+1):
        if not team[i]:
            ans += 1
            bfs(i)
    print("#{} {}".format(tc, ans))