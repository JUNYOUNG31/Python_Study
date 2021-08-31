from collections import deque

dq = deque()

for i in range(100000):
    dq.append(i)

for i in range(100000):
    print(dq.popleft())