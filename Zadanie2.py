class DivNull:
    def __init__(self, div, den):
        self.div = div
        self.den = den

    @staticmethod
    def divbnull(div, den):
        try:
            return (div / den)
        except:
            return (f"На ноль делить нельзя!")


div = DivNull(10, 100)
print(DivNull.divbnull(10, 0))
print(DivNull.divbnull(110, 10))
print(div.divbnull(100, 0))