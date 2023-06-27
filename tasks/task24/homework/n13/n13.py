import os


os.chdir('tasks/task24/homework/n13')


s = open('24.txt').readline()

res = cur = s[0]

for i in range(len(s) - 1):
    if s[i] > s[i + 1]:
        cur += s[i + 1]
        res = max(res, cur, key=len)
    else:
        cur = s[i + 1]
    
print(res)
