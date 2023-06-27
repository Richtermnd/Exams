import os


os.chdir('tasks/task24/homework/n4')


s = open('24.txt').readline()
s = s.replace('C', ' ').replace('F', ' ')
s = s.split()
print(max(len(x) for x in s))
