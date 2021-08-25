front = rear = 0
N = 10  # Q size 이다.
Q = [0] * N


def enqueue(item):
    global rear
    # is_full 검사 필요
    if (rear + 1) % N == front:
        print("너 가득차서 이제 못넣어...")
    else:
        rear = (rear + 1) % N
        Q[rear] = item


def dequeue():
    global front
    # is_empty 필요
    if front == rear:
        print("비어서 꺼낼것도 없다....")
    else:
        front = (front + 1) % N
        return Q[front]


for i in range(10):
    enqueue(i)

for i in range(10):
    print(dequeue())
