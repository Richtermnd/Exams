TARGET = 63


def f(n, is_valid):
    if n == 43:
        is_valid = False

    if n > TARGET:
        return False
    
    if n < TARGET:
        return f(n + 2, is_valid) + f(2 * n - 1, is_valid) + f(2 * n + 1, is_valid)
    
    return is_valid


print(f(7, True))
