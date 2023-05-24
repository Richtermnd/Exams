import os
import shutil


for i in range(27):
    cur_dir = f'tasks/task{i + 1}'
    try:
        os.mkdir(cur_dir)
    except FileExistsError:
        pass
    levels = ['homework', 'base', 'middle', 'hard', 'pominki']
    for level in levels:
        try:
            os.mkdir(f'{cur_dir}/{level}')
        except FileExistsError:
            pass
        
        if len(os.listdir(f'{cur_dir}/{level}')) > 1:
            try:
                os.remove(f'{cur_dir}/{level}/temp.txt')
            except FileNotFoundError:
                pass
        else: 
            with open(f'{cur_dir}/{level}/temp.txt', mode='w') as f:
                f.write('File to add dir to git')