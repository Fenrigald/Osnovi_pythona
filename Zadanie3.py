def type_logger(f):
    def action(x):
               res = f(x)
               print(f'Переменная "{x}" типа {type(x)}')
    return action

@type_logger
def calc(n):
    return n + n * n

primer = calc(10)