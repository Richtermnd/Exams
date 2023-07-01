from fnmatch import fnmatch


def divs(x):
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)
    return res


def main():
    mask = '9?*55*7'
    i = 10 ** 7  # минимальное число удовлетворяющее маске
    cnt = 5
    res = []
    
    while cnt:
        if fnmatch(str(i), mask):
           res.append((i, sum(divs(i)) % 21))
           cnt -= 1
        i -= 1

    [print(a, b) for a, b in res[::-1]]

main()