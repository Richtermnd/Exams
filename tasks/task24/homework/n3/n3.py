import os


os.chdir('tasks/task24/homework/n3')


s = open('24.txt').readline()
s = s.replace('D', ' ')
s = s.split()
print(max(len(x) for x in s))
