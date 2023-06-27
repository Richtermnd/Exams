TARGET = 20


def f(n, cnt):
    if n == 9:
        cnt += 1

    if n == 12:
        cnt += 1

    if n > TARGET:
        return False
    
    if n < TARGET:
        return f(n + 1, cnt) + f(n + 3, cnt) + f(n * 2, cnt)
    
    return cnt == 2


print(f(3, 0))
