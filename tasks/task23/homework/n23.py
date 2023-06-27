TARGET = 200


def f(n, mul_cnt):
    if n > TARGET:
        return False
    
    if n < TARGET:
        if mul_cnt <= 3:
            return f(n + 2, mul_cnt) + f(n * 3, mul_cnt + 1) + f(n * 5, mul_cnt + 1)
        return False
    
    return True


print(f(2, 0))
