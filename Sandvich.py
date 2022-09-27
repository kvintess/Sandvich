class Bread:
    def __str__(self):
        return 'Я хлеб'

    def __add__(self, other):
        return Sandvich(part1=self, part2=other)

class Sausage:

    def __str__(self):
        return 'Я колбаса'

    def __add__(self, other):
        return Sandvich(part1=self, part2=other)

class Sandvich:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2