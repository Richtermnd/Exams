import os

os.chdir('tasks/task24/homework/n16')


s = open('24.txt').readline()

s = s.split('A')

res = 0
for i in range(len(s) - 1):
    res = max(res, len(s[i] + s[i + 1]) + 1)

print(res)