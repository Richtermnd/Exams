TARGET = int('11101', 2)


def f(n):
    if n > TARGET:
        return False
    
    if n < TARGET:
        return f(n + 1) + f(n << 1) + f((n << 1) + 1)  # Да, давай, подушни со своими побитовыми сдвигами.
    
    return True


print(f(int('100', 2)))
