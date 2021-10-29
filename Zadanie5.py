class Stationery:
    def __init__(self, title='instrument'):
        self.title = title

    def draw(self):
        print(f'Drawing with {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Drawing with pen {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Drawing with pencil {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Drawing with marker {self.title}')


s = Stationery()
p = Pen('white')
pncl = Pencil('black')
mrkr = Handle('red')
ml = [s, p, pncl, mrkr]
for instr in ml:
    instr.draw()