import os


os.chdir('tasks/task24/homework/n15')


s = open('24.txt').readline()
for c in 'ABCEF':
    s = s.replace(c, ' ')

s = s.split()
print(min(len(x) for x in s))
