import os

os.chdir('tasks/task24/homework/n17')


s = open('24.txt').readline()

s = s.split('D')

res = 0
for i in range(len(s) - 2):
    res = max(res, len(s[i] + s[i + 1] + s[i + 2]) + 2)

print(res)