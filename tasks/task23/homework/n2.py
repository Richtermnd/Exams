TARGET = 154


def f(n):
    if n > TARGET:
        return False
    
    if n < TARGET:
        return f(n + 1) + f(n * 2) + f(n ** 2)
    
    return True


print(f(5))
