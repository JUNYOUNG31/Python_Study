# min max
T = int(input())
for case in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    min_a = 123456789
    max_a = 0
    for i in range(N):
        if max_a < a[i]:
            max_a = a[i]
        if min_a > a[i]:
            min_a = a[i]
    print("#{} {}".format(case+1, max_a-min_a))
