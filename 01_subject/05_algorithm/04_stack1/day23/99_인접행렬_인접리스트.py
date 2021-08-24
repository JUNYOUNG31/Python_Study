#인접행렬

# 주어진 정점들의 연결관계를 2차원 리스트로 표현한 구조
#정점의 개수와 간선의 개수가 주어진다.
#
V, E = map(int, input().split())

adj_arr = [[0] * V for _ in range(V)]

for i in range(E):
    st, ed = map(int, input().split())
    adj_arr[st][ed] = 1 #여기서 끝내면 방향성있는 표시
    adj_arr[ed][st] = 1

for i in adj_arr:
    print(*i)

##########################################################

#인접 리스트

# 나와 인접한 친구들만 리스트로 만들어 저장

V, E = map(int , input().split())

adj_list = [[] for _ in range(V)]

for i in range(E):
    st, ed = map(int, input().split())
    adj_list[st].append(ed) # 요기서 멈추면 방향성이 있는친구임.
    adj_list[ed].append(st)

for i in range(V):
    print("{}번째 연결된 정점은 : {}".format(i, adj_list[i]))

###############################################################

#뭐가 더좋나

#인접행렬
# 연결되어있는지 확인하는 작업이 필요
# 간선이 별로 없을때 정점이 매우 많으면 메모리 손해 극심심
# A 와 B 라는 두개의 정점이 서로 연결되어있는지 확인이 용이

#접리스트
# 연결되어있는 친구들만 넣어놨으니 확인 불필요
# 간선이 매우 많으면 별로 이점은 없음.
# A와 B라는 두개의 정점이 서로 연결되어있는지 확인하려면 포문 한번 돌아야됨..