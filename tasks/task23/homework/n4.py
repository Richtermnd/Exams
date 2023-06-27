TARGET = 2


def f(n):
    if n < TARGET:
        return False
    
    if n > TARGET:
        return f(n - 2) + f(n - 5)
    
    return True


print(f(23))
