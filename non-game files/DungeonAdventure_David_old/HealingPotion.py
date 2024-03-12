import random
class HealingPotion:
    def __init__(self, healing_points=None):
        if healing_points == None:
            self.healing_points = random.randint(5, 15)
        else:
            self.healing_points = healing_points

    def __str__(self):
        return f"HealingPotion({self.healing_points})"

    def __repr__(self):
        return f"HealingPotion({self.healing_points})"