import os
import csv

os.chdir('d:/python/ЕГЭ/tasks/task9/homework/n10/')


def main():
    with open('9.csv') as f:
        cnt = 0
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            row = [int(x) for x in row]

            row.sort()
            cond1 = row[3] > sum(row[:3])

            cond2 = len(set(row)) == 3
            
            if cond1 and cond2:
                cnt += 1

        print(cnt)


main()