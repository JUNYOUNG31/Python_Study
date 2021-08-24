# 숫자 카드
T = int(input())
for case in range(T):
    N = int(input())
    a = int(input())
    counts = [0] * 10

    for i in range(N):
        counts[a % 10] += 1
        a = a // 10

    max_count = 0
    max_num = 0
    i = 0
    while i < 10:
        if counts[i] != 0:
            if max_count == counts[i]:
                max_num = i
            if max_count < counts[i]:
                max_count = counts[i]
                max_num = i
        i += 1

    print("#{} {} {}".format(case + 1, max_num, max_count))