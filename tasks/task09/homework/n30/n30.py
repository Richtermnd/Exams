import os
import csv

os.chdir('d:/python/ЕГЭ/tasks/task9/homework/n30/')


def main():
    with open('9.csv') as f:
        cnt = 0
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            row = [int(x) for x in row]
            x1, y1, x2, y2 = row
            cond1 = x1 // abs(x1) != x2 // abs(x2)
            cond2 = y1 // abs(y1) != y2 // abs(y2)
            cond3 = (x1 - x2) ** 2 + (y1 - y2) ** 2 <= 25
            if cond3 and (cond1 or cond2):
                cnt += 1

        print(cnt)


main()
