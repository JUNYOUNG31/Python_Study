arr = [1, 2, 3, 4]
N = 4
sel = [0] * N


def perm(idx, check: int):
    # if check == (1 << N) - 1:
    if idx == N:
        print(sel)
        return

    for j in range(N):
        if check & (1 << j):                # 해당 비트자리 사용했는지 쳌
            continue
        sel[idx] = arr[j]                   # 값 표시
        perm(idx + 1, check | (1 << j))     # 해당 자리 썼다라고 포함시키고 내려보내기


perm(0, 0)
