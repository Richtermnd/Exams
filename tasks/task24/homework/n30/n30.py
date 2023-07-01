import os


os.chdir('tasks/task24/homework/n30')


s = open('24.txt').readline().strip()
while 'XIXIX' in s:
    s = s.replace('XIXIX', 'XIX XIX')
print(s.count('XIX'))
