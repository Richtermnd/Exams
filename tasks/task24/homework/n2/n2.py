import os


os.chdir('tasks/task24/homework/n2')


s = open('24.txt').readline()
s = s.replace('C', ' ').replace('D', ' ')
s = s.split()
print(max(len(x) for x in s))
