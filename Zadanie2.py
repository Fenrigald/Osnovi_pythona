cs = [n**3 for n in range(1000) if n % 2 == 1]
print(f'Список нечетных кубов: {format(cs)}')
s = 0
s_2 = 0
for i in range(len(cs)):
    ms = str(cs[i])
    ml = list(ms)
    for j in range(len(ml)):
        ml[j] = int(ml[j])
    sym = sum(ml)
    if sym % 7 == 0:
        print(int(cs[i]))
        s += int(cs[i])
        print(f'Сумма всех чисел по заданным условиям: {s}')

for i in range(len(cs)):
    cs[i] += 17
    ms = str(cs[i])
    ml = list(ms)
    for j in range(len(ml)):
        ml[j] = int(ml[j])
    sym = sum(ml)
    if sym % 7 == 0:
        print(int(cs[i]))
        s_2 += int(cs[i])
        print(f'Сумма всех чисел по заданным условиям с добавлением 17: {s_2}')
    cs[i] = cs[i] - 17