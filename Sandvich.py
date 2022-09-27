class Bread:
    def __str__(self):
        return 'хлеб бородинский'

    def __add__(self, other):
        return Sandvich(part1=self, part2=other)

class Sausage:

    def __str__(self):
        return 'Салями'

    def __add__(self, other):
        return Sandvich(part1=self, part2=other)

class Sandvich:

    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2
    def __str__(self):
        return 'it is sandvich of '+str(self.part1)+' and '+str(self.part2)

#example
borodinsky = Bread()
salami= Sausage()
sandvich= borodinsky + salami
print(sandvich)
