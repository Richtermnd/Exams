TARGET = 12


def f(n, is_used_mul):
    if n > TARGET:
        return False
    
    if n < TARGET:
        res = f(n + 1, is_used_mul) + f(n + 2, is_used_mul)
        if not is_used_mul:
            res += f(n * 2, True)

        return res
    
    return is_used_mul


print(f(2, False))
