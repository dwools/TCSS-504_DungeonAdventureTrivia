from Adventurer import Adventurer
from Room import Room
from RoomFactory import RoomFactory
from HealingPotion import HealingPotion
import random

print("Room Test")

room = Room(row = 1, column= 1, content="H", doors="NEWS")
print("Get Healing Points")
print(room.get_healing_points())

print(room)

print("Adventurer Test")

player = Adventurer(name="Finn")
player.find_healing_potion(HealingPotion()) # take a random healing point
player.find_healing_potion(HealingPotion(20)) # take a potion with 20 healing points
player.take_healing_potion()  # Want to use the first healing potion
# player.take_healing_potion(1)  # Want to use the second healing potion
player.find_vision_potion()
pillar_name = "A"
player.pillar_found(pillar_name)
player.fall_in_pit(random.randint(1, 20))

print(player)

