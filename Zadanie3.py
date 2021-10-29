class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._inc = {"profit": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum(self._inc.values())}"


gg = Position('Andre', 'Veseluhin', 'Burevestnik', 10, 100500)
print(gg.surname)
print(gg.get_full_name())
print(gg.get_full_profit())