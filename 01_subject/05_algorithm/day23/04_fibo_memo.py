def fibo1(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n - 1) + fibo1(n - 2))
    return memo[n]


memo = [0, 1]

def fibo2(n):
    if memo2[n] == -1:
        memo2[n] = fibo2(n - 1) + fibo2(n - 2)
    return memo2[n]


N = 5
memo2 = [-1] * (N + 1)
memo2[0] = 0
memo2[1] = 1

print(fibo2(N))
print(memo2)
