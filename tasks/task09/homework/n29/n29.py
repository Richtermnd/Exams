import os
import csv

os.chdir('d:/python/ЕГЭ/tasks/task9/homework/n29/')


def main():
    with open('9.csv') as f:
        cnt = 0
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            row = [int(x) for x in row]
            x1, y1, x2, y2 = row
            cond1 = x1 == 0 or y1 == 0
            cond2 = x2 == 0 or y2 == 0

            if cond1 and cond2:
                cnt += 1

        print(cnt)


main()
