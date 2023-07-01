import os
import re


os.chdir('tasks/task24/homework/n33')


s = open('24.txt').readline().strip()
res = 0
for i in range(len(s) - 4):
    if s[i: i + 6: 2] == 'AAA':
        res += 1

print(res)
