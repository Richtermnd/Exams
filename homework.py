import sys
import os


_, task_n, n, is_dir = sys.argv

task_n = task_n.rjust(2, '0')

if os.path.exists(f'tasks/task{task_n}/homework/template.py'):
    with open(f'tasks/task{task_n}/homework/template.py', encoding='utf8') as f:
        data = f.read()
else:
    data = ''

for i in range(int(n)):
    path = f'tasks/task{task_n}/homework/'
    i = str(i + 1).rjust(2, '0')
    if int(is_dir):
        if not os.path.exists(f'{path}/n{i}/'):
            os.mkdir(f'{path}/n{i}/')
        path = f'{path}/n{i}/'
    if not os.path.exists(f'{path}/n{i}.py'):
        with open(f'{path}/n{i}.py', mode='w', encoding='utf8') as f:
            f.write(data)
