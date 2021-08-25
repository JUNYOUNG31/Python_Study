Q = []

# Q.append(1)
# Q.append(2)
# Q.append(3)
#
#
# print(Q.pop(0))
# print(Q.pop(0))
# print(Q.pop(0))
# print(Q.pop(0))


for i in range(100000):
    Q.append(i)

for i in range(100000):
    print(Q.pop(0))