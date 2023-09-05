def f(n):
    n = n // 3 if n % 3 == 0 else n - 1
    n = n // 5 if n % 5 == 0 else n - 1
    n = n // 11 if n % 11 == 0 else n - 1
    return n

def solution():
    cnt = 0
    for i in range(1, 8 * 11 * 5 * 3 + 1):
        if f(i) == 8:
            cnt += 1
    print(cnt)
    
solution()