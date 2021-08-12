def my_print(idx, N):
    print("#{}까지의 합은 {} 이다.".format(idx, N))


def my_sum(N):
    tmp = 0

    for i in range(1, N+1):
        tmp += i
        my_print(i, tmp)

    return tmp


ans = my_sum(10)

print(ans)