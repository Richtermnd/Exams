from fnmatch import fnmatch


def main():
    mask = '12*45*'
    div = 51
    closest = 1245
    closest = (closest // div + 1) * div if closest % div else closest
    for i in range(closest, 10 ** 6 + 1, div):
        if fnmatch(str(i), mask):
            print(i, i // div)


main()