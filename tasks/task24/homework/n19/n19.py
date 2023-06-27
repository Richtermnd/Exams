import os

os.chdir('tasks/task24/homework/n19')


s = open('24.txt').readline()
s = s.replace('C', 'B').replace('D', 'B').replace('O', 'A')

res = cur = 0
for shift in 0, 1:
    cur = 0
    for i in range(shift, len(s) - 1, 2):
        sub = s[i] + s[i + 1]
        if sub == 'BA':
            cur += 1
            res = max(res, cur)
        else:
            cur = 0

print(res)