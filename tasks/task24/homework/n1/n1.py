import os


os.chdir('tasks/task24/homework/n1')


s = open('24.txt').readline()
s = s.replace('A', ' ').replace('B', ' ')
s = s.split()
print(max(len(x) for x in s))
