import os
import csv

os.chdir('d:/python/ЕГЭ/tasks/task9/homework/n7/')


def main():
    with open('9.csv') as f:
        cnt = 0
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            row = [int(x) for x in row[:4]]

            row.sort()
            cond1 = row[0] * row[3] == row[1] * row[2]

            cond2 = row[2] ** 2 > row[0] * row[3]
            
            if cond1 and cond2:
                cnt += 1

        print(cnt)


main()