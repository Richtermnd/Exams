import os


os.chdir('tasks/task24/homework/n5')


s = open('24.txt').readline()
s = s.replace('A', ' ').replace('B', ' ').replace('C', ' ')
s = s.split()
print(max(len(x) for x in s))
