def fibo(N):
    global cnt
    cnt += 1
    memo[N] += 1
    if N < 2:
        return N

    return fibo(N - 1) + fibo(N - 2)


cnt = 0
memo = [0] * 20
print(fibo(15), cnt)
print(memo)
