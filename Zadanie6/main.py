import fileinput
with fileinput.input(files='nums.txt', inplace=True) as f:
    for line in f:
        if fileinput.lineno() == int(n):
            print(line.replace('1251235', num, 1).strip())
        else:
            print(line.strip())
import json
import pickle
import random
from time import perf_counter
nums = [random.random() * 10 ** 6 for _ in range(10 **6)]
