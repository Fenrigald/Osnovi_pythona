from itertools import zip_longest
import json

with open('hum.txt', 'r', encoding='utf-8') as hum, \
        open('hobby.txt', 'r', encoding='utf-8') as hobby:
    humans = hum.read().splitlines()
    hobbys = hobby.read().splitlines()
if len(humans) < len(hobbys):
    print('Error 1')
else:
    humans_hobby = dict(zip_longest(humans, hobbys, fillvalue=None))
    with open('humans_hobby_dict.txt', 'w') as n:
        json.dump(humans_hobby, n, ensure_ascii=False)

# Для работы программы необходимо создать два файла: hum.txt и hobby.txt с внесенными в них параметрами
