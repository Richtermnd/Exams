res = set()

def f(n, cnt):
    if cnt == 15:
        res.add(n)
        return
    
    cnt += 1
    f(n * 2, cnt)
    f(n * 2 + 1, cnt)


f(1, 0)
print(len(res))
