import os
import csv
from itertools import combinations


os.chdir('d:/python/ЕГЭ/tasks/task9/homework/n5/')


def main():
    with open('9.csv') as f:
        cnt = 0
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            row = [int(x) for x in row]
            
            mx = max(row)            
            cond1 = sum(row) - mx > mx
            
            row.sort()
            cond2 = row[0] + row[3] == row[1] + row[2]
            
            if cond1 and cond2:
                cnt += 1

        print(cnt)


main()