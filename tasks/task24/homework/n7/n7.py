import os


os.chdir('tasks/task24/homework/n7')


s = open('24.txt').readline()
s = s.replace('XY', 'X Y').replace('XZ', 'X Z')
s = s.split()
print(max(len(x) for x in s))
