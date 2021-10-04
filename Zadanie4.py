products = [65.12, 36.58, 38.58, 14.38, 28, 95.83, 69, 36.37, 46.28, 19, 5.43, 53.38]
print(id(products))
price=[]

for i in products:

    if type(products[products.index(i)]) == float:
        meaning = str(products[products.index(i)])
        r, kk=meaning.split('.')
        r=int(r)
        kk=int(kk)
        if r <=9:
            if kk <= 9:
                price.append(f'«0{r} руб 0{kk} коп»')
            else:
                price.append(f'«0{r} руб {kk} коп»')
        else:
            if kk<=9:

                price.append(f'«{r} руб 0{kk} коп»')

            else:
                price.append (f'«{r} руб {kk} коп»')

    elif type(products[products.index(i)]) == int:
        r = products[products.index(i)]
        kk = 00
        if r <= 9:

            price.append(f'«0{r} руб 0{kk} коп»')
        else:

            price.append(f'«{r} руб 0{kk} коп»')

products = [65.12, 36.58, 38.58, 14.38]
print(price)
print(id(products))

price.sort()
print(price)
print(id(price))

price = price[::-1]
print(price)
print(id(price))

print('Цена пяти самых дорогих товаров:')
print(price[:5])