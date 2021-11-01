class StoreMash:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель': self.name, 'Цена': self.price, 'Кол-во': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода или ввода следвющего типа техники - Q, продолжение - Enter')
        q = input(f'> ')
        if q == 'Q':
            self.my_store_full.append(self.my_store)
            print(f'Склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return StoreMash.reception(self)


class Printer(StoreMash):
    def to_print(self):
        return f'Для печати {self.numb} раз'


class Scanner(StoreMash):
    def to_scan(self):
        return f'Для скана чего-либо {self.numb} раз'


class Copier(StoreMash):
    def to_copier(self):
        return f'Для копирования чего-либо {self.numb} раз'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())