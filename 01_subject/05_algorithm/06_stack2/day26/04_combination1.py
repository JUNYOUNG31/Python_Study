N = 4
R = 2

arr = [1, 2, 3, 4]
sel = [0] * R


def comb(idx, s_idx):
    if s_idx == R:
        print(sel)
        return
    elif idx == N:
        return
    else:
        sel[s_idx] = arr[idx]
        comb(idx + 1, s_idx + 1)  # 해당 idx 번째 자리를 뽑거나
        comb(idx + 1, s_idx)  # 해당 idx 번째 자리를 뽑지않거나


comb(0, 0)