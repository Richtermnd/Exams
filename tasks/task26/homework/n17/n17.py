import os


os.chdir('d:/ЕГЭ/tasks/task26/homework/n17/')


def main():
    f = open('26.txt')
    n = int(f.readline())
    a = [int(f.readline()) for _ in range(n)]
    a.sort()

    disk1, disk2 = [], []
    while a:
        disk1.append(a.pop())
        while sum(disk1) >= sum(disk2):
            disk2.append(a.pop(0))
       
    print(len(disk1), len(disk2))


main()
