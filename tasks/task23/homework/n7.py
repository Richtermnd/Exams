TARGET = 30


def f(n, is_valid):
    if n == 12:
        is_valid = True

    if n > TARGET:
        return False
    
    if n < TARGET:
        return f(n + 1, is_valid) + f(n * 2, is_valid)
    
    return is_valid


print(f(1, False))
