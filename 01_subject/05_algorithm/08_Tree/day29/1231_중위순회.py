# 중위순회
def in_oreder(T):
    global ans
    if T <= N:
        in_oreder(T*2)
        ans += A[T]
        in_oreder(T*2 + 1)


for tc in range(1, 11):
    N = int(input())
    A = [0] * (N + 1)
    ans = ''
    for i in range(N):
        node = list(input().split())
        A[i + 1] = node[1]
    in_oreder(1)
    print("#{} {}".format(tc, ans))