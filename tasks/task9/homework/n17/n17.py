import os
import csv


os.chdir('d:/python/ЕГЭ/tasks/task9/homework/n17/')


def main():
    with open('9.csv') as f:
        cnt = 0
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            row = [int(x) for x in row]

            # row.sort()
            cond1 = row[0] == row[2] and row[1] == row[3] and row[0] != row[1]
            
            if cond1:
                cnt += 1

        print(cnt)


main()
