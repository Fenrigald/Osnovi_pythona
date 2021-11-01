class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def chislo(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        print(cls)
        print(date_as_string)
        return date1

    @staticmethod
    def validation(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        if day <= 31 and day != 0 and month <= 12 and month != 0 and year <= 3999:
            print('Данные введены верно')
            return day, month, year
        else:
            print('Ошибка ввода данных')


d = '12-10-2011'
date2 = Date.chislo(d)
is_date = Date.validation(d)