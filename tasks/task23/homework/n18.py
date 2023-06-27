TARGET = 27


def f(n, cnt):
    if n > TARGET:
        return False
    
    if n < TARGET:
        cnt += 1
        return f(n + 1, cnt) + f(n + 4, cnt) + f(n * 2, cnt)
    
    return cnt == 7


print(f(3, 0))
