import random

class Dice:
    def __init__(self) -> None:
        self.sides = 1
        self.multiplier = 1

    def roll(self, count: int = 1) -> tuple:
        rolls = [random.randint(1, self.sides) * self.multiplier for x in range(count)]
        return rolls

class D4(Dice):
    def __init__(self) -> None:
        super().__init__()
        self.sides = 4
        self.multiplier = 1

class D6(Dice):
    def __init__(self) -> None:
        super().__init__()
        self.sides = 6
        self.multiplier = 1

class D8(Dice):
    def __init__(self) -> None:
        super().__init__()
        self.sides = 8
        self.multiplier = 1

class D10(Dice):
    def __init__(self) -> None:
        super().__init__()
        self.sides = 10
        self.multiplier = 1

class D12(Dice):
    def __init__(self) -> None:
        super().__init__()
        self.sides = 12
        self.multiplier = 1

class D20(Dice):
    def __init__(self) -> None:
        super().__init__()
        self.sides = 20
        self.multiplier = 1

class D100(Dice):
    def __init__(self) -> None:
        super().__init__()
        self.sides = 100
        self.multiplier = 1