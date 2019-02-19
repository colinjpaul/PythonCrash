from random import randint

class Die:

    def __init__(self, sides=6):
        """Initialise the battery's attributes"""
        self.sides = sides

    def roll_die(self, rolls):
        self.rolls = rolls
        i = 0
        while i < self.rolls:
            x = randint(1, self.sides)
            print(x)
            i = i + 1

my_die = Die(20)
my_die.roll_die(10)





