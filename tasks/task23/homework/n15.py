TARGET = 51


def transform(n):
    res = 0
    for i, num in enumerate(str(n)[::-1]):
        a = num != '9'
        res += (int(num) + a) * 10 ** i        
    return res


def f(n):
    if n > TARGET:
        return False
    
    if n < TARGET:
        return f(n + 1) + f(transform(n))
    
    return True


print(f(25))
