# from items import Item
import random
from item_pit_trap import PitTrap
from item_health_potion import HealthPotion
from object_coordinates_generator import ValidCoordsGenerator

class ItemFactory:

    def get_location(self):
        coords = ValidCoordsGenerator()
        coords.generate_coords()
        location = coords.get_random_coords()
        return location

    def create_health_potion(self):
        # location = self.get_location()
        add_health = random.randint(5, 15)
        return HealthPotion(add_health)

    def create_pit_trap(self):
        # location = self.get_location()
        damage = random.randint(1, 20)
        return PitTrap(damage)

    def choose_item(self):
        choice = random.randint(1,2)
        if choice == 1:
            item_choice = self.create_health_potion()
        else:
            item_choice = self.create_pit_trap()
        return item_choice


    # def pit_trap(self):
    #     """ Pit Trap item to be placed in the Pit Trap room. """
    #
    #     damage = random.randint(1, 20)
    #     print(f"You have fallen in a pit and taken {damage} damage")
    #     return damage
    #
    # # Potions
    #
    # def health_potion(self):
    #     """ Health potion consumable. """
    #     add_health = random.randint(5, 15)
    #     print(f"You feel invigorated and restore {add_health} points of health")
    #     return add_health

if __name__ == "__main__":
    u = ItemFactory()
    trap = u.create_pit_trap()
    print(f"location = {trap.get_location()}, health_points = {trap.get_health_change()}")

