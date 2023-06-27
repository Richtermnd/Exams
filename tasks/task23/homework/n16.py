TARGET = 20


def f(n):
    if n > TARGET:
        return False
    
    if n < TARGET:
        res = f(n + 1)
        if n % 2 == 0:
            res += f(n * 1.5)
        return res
    
    return True


print(f(1))
