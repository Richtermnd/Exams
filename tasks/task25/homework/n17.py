from math import ceil

def div(x: int) -> list[int]:
    res = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res.add(i)
            res.add(x // i)

    return sorted(res)


def main():
    """ Основная теорема арифметики """
    start = ceil(106_732_567 ** 0.25)
    finish = int(152_673_836 ** 0.25)
    print(start, finish)
    for i in range(start, finish):
        divs = div(i)
        if len(divs) == 2:
            print(i ** 4, max(div(i ** 4)[1:-1]))


main()
