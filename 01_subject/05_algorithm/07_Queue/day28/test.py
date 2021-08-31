# 가위 1, 바위 2, 보 3

def win(num_a, rcp_a, num_b, rcp_b):
    #가위바위보가 위의 숫자처럼 정해져 있으니 활용가능
    if rcp_b - rcp_a == 1 or rcp_b - rcp_a == -2:
        return num_b, rcp_b
    else:
        return num_a, rcp_a

def divided(st, ed):
    #한사람만 남았을때
    if st == ed:
        return st, people[st]
    mid = (st + ed) // 2

    return win(*divided(st, mid), *divided(mid+1, ed))


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    people = list(map(int, input().split()))

    ans = divided(0, N-1)

    print("#{} {}".format(tc, ans[0]+1))
