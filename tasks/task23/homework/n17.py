from functools import lru_cache


TARGET = ...

def f(n):
    if n > TARGET:
        return False
    
    if n < TARGET:
        return f(n +2) + f(n + 4) + f(n + 5)
    
    return True

for i in range(1000):
    TARGET = i  # Не бейте, пж.
    if f(31) == 1001:
        print(i)