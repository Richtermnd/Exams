import os


os.chdir('d:/python/ЕГЭ/tasks/task17/homework/n16')


def main():
    a = [int(x) for x in open('17.txt')]
    mod17 = []
    mod11 = []

    for x in a:
        if x % 11 == 0:
            mod11.append(x)
        if x % 17 == 0:
            mod17.append(x)

    if len(mod11) > len(mod17):
        print(len(mod11), min(mod11))
    else:
        print(len(mod17), max(mod17))

main()