from functools import lru_cache


TARGET = 40


@lru_cache(None)
def f(n, odd_cnt):
    odd_cnt += n % 2

    if n > TARGET:
        return False
    
    if n < TARGET:
        return f(n + 1, odd_cnt) + f(n + 2, odd_cnt) +  f(n * 2, odd_cnt)
    
    return odd_cnt == 1


print(f(2, 0))
