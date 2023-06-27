import os


os.chdir('tasks/task24/homework/n8')


s = open('24.txt').readline()
while 'PP' in s:
    s = s.replace('PP', 'P P')

s = s.split()
print(max(len(x) for x in s))
