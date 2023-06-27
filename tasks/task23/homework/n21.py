TARGET = 15


def f(n, is_rev_mul):
    if n > TARGET:
        return False
    
    if n < TARGET:
        res = f(n + 1, False) + f(n + 2, False)
        if not is_rev_mul:
            res +=f(n * 2, True) 
        return res
    
    return True


print(f(1, False))
