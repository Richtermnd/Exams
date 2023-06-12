import sys
import os


_, task_n, n, is_dir = sys.argv

if os.path.exists(f'tasks/task{task_n}/homework/template.py'):
    with open(f'tasks/task{task_n}/homework/template.py', encoding='utf8') as f:
        data = f.read()
else:
    data = ''

for i in range(int(n)):
    path = f'tasks/task{task_n}/homework/'
    if int(is_dir):
        if not os.path.exists(f'{path}/n{i + 1}/'):
            os.mkdir(f'{path}/n{i + 1}/')
        path = f'{path}/n{i + 1}/'
    if not os.path.exists(f'{path}/n{i + 1}.py'):
        with open(f'{path}/n{i + 1}.py', mode='w', encoding='utf8') as f:
            f.write(data)
