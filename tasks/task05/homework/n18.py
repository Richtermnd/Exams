def f(n):
    r = str(n)
    r1 = sum(int(x) for x in r if int(x) % 2 == 0)
    r2 = sum(int(x) for x in r[1::2])
    return abs(r1 - r2)


def solution():
    for i in range(1, 1000):
        if f(i) == 9:
            print(i)
            break

    
solution()