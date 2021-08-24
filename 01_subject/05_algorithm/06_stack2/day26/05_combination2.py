N = 4
R = 3

arr = [1, 2, 3, 4]
sel = [0] * R  # 내가 뽑을 공간 미리 확보


def comb(idx, s_idx):   # idx : arr 에서 시작하는 위치
    if s_idx == R:      # s_idx : 내가 뽑고 있는 위치
        print(sel)
        return

    for i in range(idx, N):
        sel[s_idx] = arr[i]
        comb(i + 1, s_idx + 1)


comb(0, 0)
