class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def mass(self, w=25, t=5):
        m = self._length * self._width * w * t
        return f"Mass = {m/1000}"
r = Road(5000, 20)
print(r.mass())