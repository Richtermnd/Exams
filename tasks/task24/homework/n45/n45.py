import os


os.chdir('tasks/task24/homework/n45')


def longest_chain(s):
    res = 0
    for i in range(len(s) - 1):
        c = s[i]
        j = i
        while j + 1 < len(s) and s[j] == c:
            j += 1
        res = max(res, j - i)
    # print(s, res)
    return res


def main():
    full = ''
    row = ''
    for s in open('24.txt'):
        s = s.strip()
        row = max(row, s, key=longest_chain)
        full += s
        
    most_common = max(row, key=lambda x: (row.count(x), -ord(x)))
    print(most_common, full.count(most_common), sep='')


main()
