class Bread:
    def __init__(self):
        return 'Я хлеб'

    def __add__(self, other):
        return Sandvich(part1=self, part2=other)

class Sausage