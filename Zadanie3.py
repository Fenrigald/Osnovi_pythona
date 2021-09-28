for i in range(1, 101):
    if i % 10 == 0 or 11 <= i <= 14 or 5 <= i % 10 <= 9:
        print(f'{i} процентов')
    elif i % 10 == 1:
        print(f'{i} процент')
    elif 2 <= i % 10 <= 4:
        print(f'{i} процента')
