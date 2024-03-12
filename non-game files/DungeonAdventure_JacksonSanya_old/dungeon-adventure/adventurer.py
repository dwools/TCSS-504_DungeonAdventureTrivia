import random

from items import Items

"""
Has a name

Contains at least the following:

Hit Points - initially set to 75 - 100 upon creation (randomly generate - you can change the range) 

The number of Healing Potions 

The number of Vision Potions 

Which Pillars have been found 

Ability to move in Dungeon (you might decide to place this behavior elsewhere)

Increases or decreases the Hit Points accordingly

Contains a _ _ str _ _ () method that builds a String containing:
Name
Hit Points
Total Healing Potions
Total Vision Potions
List of Pillars Pieces Found

NOTE: The Adventurer and the Dungeon will need to interact. When the Adventurer walks into a room if there is a potion in
the room, the Adventurer automatically picks up the potion. Likewise if there is a pit in the room, the Adventurer automatically
falls in the pit and takes a Hit Point loss. These changes obviously affect the room. For example, the Adventurer walks into a
room that contains a Healing Potion. The Adventurer will pick up the potion, changing the Adventurer's potion total, as well as
changing the room's potion total.
"""


class Adventurer(Items):

    def __init__(self, name="test"):
        super().__init__()
        self.__adventurer_name = name
        self.__health_max = random.randint(75, 100)
        self.__current_health = self.__health_max
        self.__vision_active = False

        # Backpack
        self.__pillars = []
        self.__potions = [["Health Potions", 0], ["Vision Potions", 0]]

    def __str__(self):

        return f"Adventurer Name: {self.__adventurer_name}, Current Health: {self.__current_health}/{self.__health_max}\n" \
            + f"Health Potions: {self.__potions[0][1]}, Vision Potions: {self.__potions[1][1]}\n" \
            + f"Pillars found: {self.__pillars}\n\n"

    def get_adventurer_name(self):
        return f"{self.__adventurer_name}"

    def remove_from_backpack(self, item):

        if item == Items.health_potion:
            print("The potion was consumed.")
            self.__potions[0][1] -= 1
            print(self.__potions)

        elif item == Items.vision_potion:
            print("The potion was consumed.")
            self.__potions[1][1] -= 1
            print(self.__potions)

    def add_to_backpack(self, item):

        if item == Items.health_potion:
            self.__potions[0][1] += 1
            print("You have added the health potion to your bag!")
            print(f"{self.__potions}")

        elif item == Items.vision_potion:
            self.__potions[1][1] += 1
            print("You have added the vision potion to your bag!")
            print(f"{self.__potions}")

        elif item == Items.pillar_of_inheritance:
            self.__pillars.append(Items.pillar_of_inheritance(self))
            print(self.__pillars)

        elif item == Items.pillar_of_polymorphism:
            self.__pillars.append(Items.pillar_of_polymorphism(self))
            print(self.__pillars)

        elif item == Items.pillar_of_abstraction:
            self.__pillars.append(Items.pillar_of_abstraction(self))
            print(self.__pillars)

        elif item == Items.pillar_of_encapsulation:
            self.__pillars.append(Items.pillar_of_encapsulation(self))
            print(self.__pillars)

    def update_health(self, source):

        if source == Items.pit_trap:
            self.__current_health -= Items.pit_trap(self)
            print(f"\nYour health is now: {self.__current_health}/{self.__health_max}")

        elif source == Items.health_potion:
            self.__current_health += Items.health_potion(self)

            if self.__current_health > self.__health_max:
                self.__current_health = self.__health_max
                print(f"\nYour health is now: {self.__current_health}/{self.__health_max}")

            else:
                print(f"\nYour health is now: {self.__current_health}/{self.__health_max}")

    def update_vision(self, source):

        # Should have a "while loop" to time the length of the potion
        if source == Items.vision_potion:
            self.__vision_active += Items.vision_potion(self)
        return self.__vision_active



