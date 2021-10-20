import os

settings = {}
with open('config.yaml') as o:
    lines = dict(map(str.split, o.readlines()))
basedir = lines.pop('base')
for x, z in lines.items():
    os.makedirs(os.path.join(os.curdir, basedir, x), exist_ok=True)
    print(f'Создан каталог: {x}')
    for i in z.split(','):
        with open(os.path.join(os.curdir, basedir, x, i), "w") as f:
            print(f'Создан файл: {i} в каталоге {x}')