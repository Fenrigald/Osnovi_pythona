def num_translate(key):
    print(numerals_dict.get(key))

def num_translate_adv(key):
    if (my_num[:1].isupper()) == True:
        for i in numerals_eng:
            numerals_eng[numerals_eng.index(i)] = numerals_eng[numerals_eng.index(i)].capitalize()
        for i in numerals_rus:
            numerals_rus[numerals_rus.index(i)] = numerals_rus[numerals_rus.index(i)].capitalize()

my_num = input('Print number in 1 to 10: ')
numerals_eng = ['one','two','three','four','five','six','seven','eight','nine','ten']
numerals_rus = ['один','два','три','четыре','пять','шесть','семь','восемь','девять','десять']

num_translate_adv(my_num)
numerals_dict = dict(zip(numerals_eng,numerals_rus))
num_translate(my_num)