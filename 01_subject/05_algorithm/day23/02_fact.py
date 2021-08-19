def fact(N: int) -> int:
    # base_case
    if N == 1:
        return 1
    # recursive_case
    ans = N * fact(N-1)
    return ans


print(fact(4))
