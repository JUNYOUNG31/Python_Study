# 최소 신장 트리
def make_set(x):                                                  # 대표원소 선택
    p[x] = x


def find_set(x):                                                  # 대표원소 찾기
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):                                                  # 묶기
    p[find_set(y)] = find_set(x)


T = int(input())                                                  # case 수 입력
for tc in range(1, T+1):                                          # case 반복
    V, E = map(int, input().split())                              # V : 마지막 노드 번호, E 간선의 개수
    edges = [list(map(int, input().split())) for _ in range(E)]   # 입력
    edges.sort(key=lambda x: x[2])                                # 가중치를 기준으로 정렬
    p = [0] * (V+1)
    for i in range(V+1):
        make_set(i)
    ans = 0
    pick = 0                                                      # 간선을 선택 횟수
    idx = 0                                                       # 간선 리스트를 가리키는 인덱수
    while pick < V:                                               # 마지막 노드까지
        n1 = edges[idx][0]                                        # 각 간선의 대표 원소
        n2 = edges[idx][1]                                        # 각 간선의 원소
        if find_set(n1) != find_set(n2):                          # 두개의 대표원소가 같지않으면
            union(n1, n2)                                         # 두개를 묶어주고
            pick += 1                                             # 간선 선택하고
            ans += edges[idx][2]                                  # 선택했으니까 가중치 추가
        idx += 1                                                  # idx 추가
    print("#{} {}".format(tc, ans))