import os

os.chdir('tasks/task24/homework/n22')


s = open('24.txt').readline()
s = s.replace('B', 'A').replace('2', '1')

res = cur = 0
for shift in 0, 1, 2:
    cur = 0
    for i in range(shift, len(s) - 2, 3):
        sub = ''.join(s[i:i + 3])
        if sub == '11A':
            cur += 1
            res = max(res, cur)
        else:
            cur = 0

print(res)