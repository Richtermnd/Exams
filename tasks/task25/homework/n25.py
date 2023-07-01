from fnmatch import fnmatch


def main():
    mask = '1?2139*4'
    div = 2023
    closest = 1021394
    closest = (closest // div + 1) * div if closest % div else closest
    for i in range(closest, 10 ** 10 + 1, div):
        if fnmatch(str(i), mask):
            print(i, i // div)


main()