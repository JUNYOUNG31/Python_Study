# 전기버스
T = int(input())
for case in range(T):
    K, N, M = map(int, input().split())
    charging = map(int, input().split())

    station = [0]*(N+1)

    for i in charging:    # 충전소를 표시
        station[i] = 1

    # for i in range(M):        # 위랑 같은 표현
    #     station[charging[i]] = 1

    bus_idx = 0  # 버스 위치
    ans = 0

    # 무한루프 주의
    while True:
        # 버스가 이동할 수 있는 만큼 무조건 가기
        bus_idx += K
        if bus_idx >= N: break # 종점에 도착하거나 종점을 지나는 경우

        for i in range(bus_idx, bus_idx-K, -1):
            # if station[i] == 1:
            if station[i]:
                ans += 1
                bus_idx = i
                break
        else:
            ans = 0
            break

    print("#{} {}".format(case+1, ans))