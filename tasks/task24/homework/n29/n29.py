import os


os.chdir('tasks/task24/homework/n29')


s = open('24.txt').readline().strip()
print(s.count('BOSS') - s.count('JBOSS') - s.count('BOSSJ') + s.count('JBOSSJ'))  # EZ
