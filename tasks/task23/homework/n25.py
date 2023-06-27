TARGET = 25


def f(n, cnt):
    cnt += n % 2 == 0

    if n > TARGET:
        return False
    
    if n < TARGET:
        return f(n + 1, cnt) + f(n + 3, cnt) + f(n + 5, cnt)
    
    return cnt == 6


print(f(3, 0))
