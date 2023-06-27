TARGET = ...


def f(n):
    if n > TARGET:
        return False
    
    if n < TARGET:
        return f(n)
    
    return True


print(f(1))
