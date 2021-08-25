def enqueue(item):
    global rear
    # is_full 검사 필요
    if (rear + 1) % N == front:
        return
    else:
        rear = (rear + 1) % N
        Q[rear] = item


def dequeue():
    global front
    # is_empty 필요
    if front == rear:
        return
    else:
        front = (front + 1) % N
        return Q[front]


for tc in range(1, 11):                        # case 10 반복
    T = int(input())                           # case 번호
    Password = list(map(int, input().split())) # 숫자 입력
    front = rear = -1                          # queue
    N = 8                                      # Q size 이다.
    Q = [0] * N                                # 빈 리스트 생성

    for i in range(N):                         # Q 에 넣기
        enqueue(Password[i])                   # enQueue
    a = 0
    while True:                                # 반복
        a += 1                                 # - 할 값 1씩 추가
        if a > 5:                              # 5보다 크면 1로
            a = 1
        result = Q.pop(0)                      # 첫번째 값 삭제
        result -= a                            # -a
        if result <= 0:                        # 0보다 작거나 같으면
            result = 0                         # 0으로 바꾸고
            Q.append(0)                        # 마지막에 삽입
            break
        Q.append(result)                       # 아니면 맨뒤에 추가

    print("#{}".format(tc), end=" ")           # 출력
    print(*Q)