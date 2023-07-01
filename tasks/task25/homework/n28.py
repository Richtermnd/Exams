from fnmatch import fnmatch


def divs(x):
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)
    return res


def main():
    mask = '?6*6*?6'
    cnt = 7
    i = 6606
    while cnt:
        if fnmatch(str(i), mask):
            if i % 6 == i % 7 == i % 8 == 0:
                print(i, sum(divs(i)))
                cnt -= 1
        i += 1


main()