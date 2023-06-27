import os


os.chdir('tasks/task24/homework/n9')


s = open('24.txt').readline()
s = s.replace('XZZY', 'XZZ ZZY')

s = s.split()
print(max(len(x) for x in s))
