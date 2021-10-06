# 컨테이너 운반

# 화물이 실려 있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반하려고 한다.
# 트럭당 한 개의 컨테이너를 운반 할 수 있고, 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다.
# 컨테이너마다 실린 화물의 무게와 트럭마다의 적재용량이 주어지고, A도시에서 B도시로 최대 M대의 트럭이
# 편도로 한번 만 운행한다고 한다.
# 이때 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물의 전체 무게가 얼마인지
# 출력하는 프로그램을 만드시오.
# 화물을 싣지 못한 트럭이 있을 수도 있고, 남는 화물이 있을 수도 있다. 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.

# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 컨테이너 수 N과 트럭 수 M이 주어지고, 다음 줄에 N개의 화물이 무게wi,
# 그 다음 줄에 M개 트럭의 적재용량 ti가 주어진다.
# 1<=N, M<=100, 1<=wi, ti<=50

T = int(input())                                # case 입력
for tc in range(1, T+1):                        # case 반복
    N, M = map(int, input().split())            # 트럭과 컨테이너
    visited = [0] * M                           # 방문 체크
    weight = list(map(int, input().split()))    # 화물의 무게
    truck = list(map(int, input().split()))     # 트럭의 용량
    weight.sort()                               # 정렬
    truck.sort()                                # 정렬
    for i in range(N-1, -1, -1):                # 큰거부터 넣기
        for j in range(M-1, -1, -1):
            if weight[i] <= truck[j] and visited[j] == 0:  # 방문안했으면
                visited[j] = weight[i]                     # 화물무게로 바꿔주고
                break
    ans = sum(visited)                                     # 화물무게의 합
    print("#{} {}".format(tc, ans))