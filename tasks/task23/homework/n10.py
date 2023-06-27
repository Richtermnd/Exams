TARGET = 63


def f(n, cond1, cond2):
    if n == 6:
        cond1 = False

    if n == 25:
        cond2 = True
    
    if n > TARGET:
        return False
    
    if n < TARGET:
        return f(n + 2, cond1, cond2) + f(n * 3, cond1, cond2)
    
    return cond1 and cond2


print(f(1, True, False))
