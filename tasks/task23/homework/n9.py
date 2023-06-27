TARGET = 5


def f(n, is_valid):
    if n == 43:
        is_valid = True

    if n < TARGET:
        return False
    
    if n > TARGET:
        return f(n - 8, is_valid) + f(n // 2, is_valid)
    
    return is_valid


print(f(102, False))
