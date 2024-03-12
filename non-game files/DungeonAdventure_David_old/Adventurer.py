import random
from HealingPotion import HealingPotion


class Adventurer:
    """Creates adventurer features: name, hit points, healing potions, vision potions, pillar_pieces_found"""
    def __init__(self, name):
        self.name = name
        self.hit_points = random.randint(75, 100)
        self.healing_potions = []
        self.vision_potions = 0
        self.pillar_pieces_found = []  # ['A', 'E', 'I', 'P']
        self.location = (0, 0)  # Is this the correct starting location?

    """Sets that when player takes a potion they heal 5-15 hit points (random)"""
    def take_healing_potion(self):
        if 0 < len(self.healing_potions):
            healing_potion = self.healing_potions.pop()
            self.hit_points += healing_potion.healing_points
            print(f"Drinking that potion increased your health by {healing_potion.healing_points}!"
                  f"\n\nYou now have {self.hit_points} Hit Points.")
        else:
            print("You don't have any healing potions!")
            pass

    """Decrement vision potion count when one is taken"""
    def take_vision_potion(self):
        self.vision_potions -= 1

    """Get the coordinates of the room"""
    def getRoom(self, row,col):
        return self.maze[row][col]

    """Set that when a player falls in a pit they take 1-20 damage, decrease in hit points (random) """
    def fall_in_pit(self, damage_taken):
        self.hit_points -= damage_taken #random.randint(1, 20)

    """Set that when a player finds a healing potion in a room it increase the total amount of potions by 1 """

    def find_healing_potion(self, healing_potion: HealingPotion):
        self.healing_potions.append(healing_potion)

    """Set that when a player finds a vision potion in a room it increase the total amount of potions by 1 """
    def find_vision_potion(self):
        self.vision_potions += 1

    """Set that when a player finds a pillar piece in a room it adds the name of the pillar found"""
    def pillar_found(self, pillar_name):
        self.pillar_pieces_found.append(pillar_name)

    """Builds a String containing: Name, Hit Points, Total Healing Potions, Total Vision Potions, Pillar Pieces Found"""
    def __str__(self):
        #return f'Name: {self.name}, Hit Points: {self.hit_points}, Healing Potions: {self.healing_potions}, Vision Potions: {self.vision_potions}, Pillars Pieces Found: {", ".join(self.pillar_pieces_found)}'
        return f'Name:{self.name}\n-----------\n Hit Points: {self.hit_points}\n Healing Potions: {self.healing_potions}\n Vision Potions: {self.vision_potions}\n Pillars Pieces Found: {", ".join(self.pillar_pieces_found)}\n'

# player = Adventurer(name="Finn")
# healing_potion1 = healing_potion(10)
# healing_potion2 = healing_potion(15)
# player.find_healing_potion(healing_potion1)
# player.find_vision_potion()
# player.pillar_found("Abstraction")
# player.fall_in_pit(damage_taken)
#
# #healing potion and pit damage not working
#
# print(player)


# player = Adventurer(name="Finn")
# #healing_potion1 = random.randint(5, 15)
# # healing_potion2 = random.randint(5, 15)
#
# player.find_healing_potion(HealingPotion()) # take a random healing point
# player.find_healing_potion(HealingPotion(20)) # take a potion with 20 healing points
# player.take_healing_potion()  # Want to use the first healing potion
# # player.take_healing_potion(1)  # Want to use the second healing potion
# player.find_vision_potion()
# player.pillar_found("Abstraction")
# player.fall_in_pit(random.randint(1, 20))
#
# print(player)

