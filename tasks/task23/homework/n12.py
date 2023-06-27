TARGET = 15


def f(n):
    if n > TARGET:
        return False
    
    if n < TARGET:
        return f(n + 1) + f(n * 2) + f(n * 2 + 1) + f(n * 10)
    
    return True


print(f(1))
