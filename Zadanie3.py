class Err:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Вводите значения. Разделяйте с помощью Enter - '))
                self.my_list.append(val)
                print(f'Список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение")
                y_or_n = input(f'Попробовать еще раз? Yes/No ')

                if y_or_n == 'Yes':
                    print(try_except.my_input())
                elif y_or_n == 'No':
                    return f'Программа завершена'
                    break
                else:
                    return f'Некорректный ответ. Программа завершена'


try_except = Err(1)
print(try_except.my_input())