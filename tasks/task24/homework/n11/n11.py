import os


os.chdir('tasks/task24/homework/n11')


s = open('24.txt').readline()

res = cur = 1
for i in range(len(s) - 1):
    if s[i] <= s[i + 1]:
        cur += 1
        res = max(res, cur)
    else:
        cur = 1
    
print(res)
