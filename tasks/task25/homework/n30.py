from fnmatch import fnmatch


def main():
    masks = ['*0??3*', '*4??2', '*1*']
    i = 700_000
    i = (i // 13 + 1) * 13
    cnt = 5
    while cnt:
        if not any(fnmatch(str(i), mask) for mask in masks):
            print(i, sum(int(x) for x in str(i)))
            cnt -= 1
        i += 13




main()