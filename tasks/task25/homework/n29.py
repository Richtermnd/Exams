from fnmatch import fnmatch


def divs(x):
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)
    return res


def main():
    mask = '14?4*'
    i = 10 ** 7
    i = i // 217 * 217
    cnt = 7
    res = []
    while cnt:
        if fnmatch(str(i), mask):
            res.append((i, sum(x for x in divs(i) if x % 2)))
            cnt -= 1

        i -= 217
    [print(*elem) for elem in res[::-1]]



main()