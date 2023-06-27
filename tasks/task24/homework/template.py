import os


os.chdir('tasks/task24/homework/n_')


s = open('24.txt').readline()
print(max(len(x) for x in s))
