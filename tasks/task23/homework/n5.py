TARGET = 2


def f(n):
    if n < TARGET:
        return False
    
    if n > TARGET:
        return f(n - 1) + f(n - 3) + f(n // 3)
    
    return True


print(f(22))
