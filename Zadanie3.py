import random
def get_jokes(n,i):
    while i<=n:
        a=random.choice(nouns)
        nouns.remove(a)
        b=random.choice(adverbs)
        adverbs.remove(b)
        c=random.choice(adjectives)
        adjectives.remove(c)
        my_list_jokes.append(f'{a} {b} {c}')
        i+=1
    return print(my_list_jokes)


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
my_list_jokes=[]
n= int(input('Введите n шуток: '))
i=1
get_jokes(n,i)