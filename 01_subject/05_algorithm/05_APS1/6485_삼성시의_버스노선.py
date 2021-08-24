# # 삼성시의 버스 노선
# def bus_count(bus_stop):
#     cnt = 0
#     for i in range(N):
#         if bus_route[i][0] <= bus_stop <= bus_route[i][1]:
#             cnt += 1
#     return cnt
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     bus_route = []
#
#     for i in range(N):
#         a, b = map(int, input().split())
#         bus_route.append((a, b))
#
#     P = int(input())
#     ans = []
#
#     for i in range(P):
#         C = int(input())
#         ans.append(bus_count(C))
#
#     print("#{}".format(tc), end=' ')
#     print(' '.join(map(str, ans)))
#
#
# #############################################
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#
#     start = [0] * 5001
#     end = [0] * 5001
#     bus_stop = [0] * 5001
#
#     for i in range(N):
#         A, B = map(int, input().split())
#         start[A] += 1
#         end[B] += 1
#
#     for i in range(len(bus_stop)-1):
#         bus_stop[i+1] =bus_stop[i] - end[i] + start[i+1]
#
#     P = int(input())
#     print("#{}".format(tc), end=" ")
#     for i in range(P):
#         C = int(input())
#         print(bus_stop[C], end=" ")
#     print()
#
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    bus_stop = [0] * 5001

    for i in range(N):
        A, B = map(int, input().split())

        for j in range(A, B+1):
            bus_stop[j] += 1
    P = int(input())
    print("#{}".format(tc), end=" ")
    for i in range(P):
        C = int(input())
        print(bus_stop[C], end=" ")
    print()