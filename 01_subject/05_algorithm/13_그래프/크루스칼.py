## ㅋㅋ 실은 5249번 문제임

def make_set(x):
    p[x] = x

def find_set(x):
    #패스 컴프레쇼오온이 적용된 뽜인드셋
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

#랭크는 고려x
def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())  # V : 마지막 정점의 번호, E 간선의 개수

    edges = [list(map(int, input().split())) for _ in range(E)]

    edges.sort(key=lambda x: x[2]) # 가중치를 기준으로 정렬

    p = [0] * (V+1)
    for i in range(V+1):
        make_set(i)

    # p = [i for i in range(V+1)]
    # p = list(range(V+1))         p의 결과물은 몽땅 같아.~~~


    ans = 0
    pick = 0 # 간선을 선택 횟수
    idx = 0  # 간선 리스트를 가리키는 인덱수

    while pick < V: #간선의 개수는 정점수 -1개 이지만 이번에는 마지막번호이니까 쪼금 다름 ㅋ
        x = edges[idx][0]
        y = edges[idx][1]

        if find_set(x) != find_set(y):
            union(x, y)
            pick += 1 # 간선 선택한거임
            ans += edges[idx][2] # 선택했으니까 가중치 추가

        idx += 1

    print("#{} {}".format(tc, ans))
