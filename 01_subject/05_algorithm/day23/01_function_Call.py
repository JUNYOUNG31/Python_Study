def f2():
    print("f2 시작")
    print("f2 끝")


def f1():
    print("f1 시작")

    print(f2())
    print("f1 끝")
    return "깔깔"


print("main 시작")
print(f1())
print("main 끝")
