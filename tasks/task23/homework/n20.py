res = set()

def f(n, cnt):
    if cnt == 8:
        if 1000 <= n <= 1024:
            res.add(n)
        return
    
    f(n + 1, cnt + 1)
    f(n + 5, cnt + 1)
    f(n * 3, cnt + 1)


f(1, 0)
print(len(res))
