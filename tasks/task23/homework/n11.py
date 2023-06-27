TARGET = 23


def f(n, cond1, cond2):
    if n == 8:
        cond1 = True

    if n == 11 or n == 18:
        cond2 = False

    if n > TARGET:
        return False
    
    if n < TARGET:
        return f(n + 1, cond1, cond2) + f(n + 2, cond1, cond2) + f(n * 3, cond1, cond2)
    
    return cond1 and cond2


print(f(4, False, True))
