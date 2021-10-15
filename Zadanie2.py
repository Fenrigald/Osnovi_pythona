tutor = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']

klass = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

def gen():
    i = 0
    j = 0
    while i < len(klass):
        if i >= len(tutor):
            yield (None, klass[i])
            i += 1
            j += 1
            break
        else:
            yield (tutor[j], klass[i])
            i += 1
            j += 1

for gen in gen():
    print(gen)