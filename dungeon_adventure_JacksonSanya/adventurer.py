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
    """ Adventurer Class. Interacts with rooms and the consumable items in said rooms.
    Pillar and potion counts are tracked within the class. """

    def __init__(self, name=input("Welcome adventurer, please tell me your name: "), x=None, y=None):
        super().__init__()
        self.__adventurer_name = name
        self.__health_max = random.randint(75, 100)
        self.__current_health = self.__health_max
        self.__vision_active = False

        # Adventurer's position in the dungeon
        self.__position = [x, y]

        # Backpack
        self.__pillars = []
        self.__potions = [["Health Potions", 0], ["Vision Potions", 0]]

    def __str__(self):
        """ Overwrites the built-in string function. """

        return f"Adventurer Name: {self.__adventurer_name}, Current Health: {self.__current_health}/{self.__health_max}\n" \
            + f"Health Potions: {self.__potions[0][1]}, Vision Potions: {self.__potions[1][1]}\n" \
            + f"Pillars found: {self.__pillars}\n\n"

    def print_stats(self):
        print(self.__str__())

    def get_adventurer_name(self):
        """ Get method for the adventurers name. """

        return f"{self.__adventurer_name}"

    def get_potions(self):
        """ Get method for count of potions. """

        return self.__potions

    def get_adventurer_position(self):
        """ Get method for adventurer position in the dungeon. """

        return f"{self.__position}"

    def set_adventurer_position(self, position):
        """ Set method for adventurer position in the dungeon. """

        self.__position = position

    def get_obtained_pillars(self):
        """ Get method for retrieving obtained pillars. """

        return f"{self.__pillars}"

    def remove_from_backpack(self, item):
        """ Remove an item from the backpack if it is consumed."""

        if item == Items.health_potion:
            print("The potion was consumed.")
            self.__potions[0][1] -= 1
            print(self.__potions)

        elif item == Items.vision_potion:
            print("The potion was consumed.")
            self.__potions[1][1] -= 1
            print(self.__potions)

    def add_to_backpack(self, item):
        """ Add an item to the backpack. """

        if item == Items.health_potion:
            self.__potions[0][1] += 1
            print("You have added the health potion to your bag!")
            print(f"{self.__potions}")

        elif item == Items.vision_potion:
            self.__potions[1][1] += 1
            print("You have added the vision potion to your bag!")
            print(f"{self.__potions}")

        # Adding pillars to the backpack
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
        """ Updates the player's health. """

        # if the source of the update is pit trap, damage
        if source == Items.pit_trap:
            self.__current_health -= Items.pit_trap(self)
            print(f"\nYour health is now: {self.__current_health}/{self.__health_max}")

        # if the source of the update is a potion, heal
        elif source == Items.health_potion:
            self.__current_health += Items.health_potion(self)

            # Prevents healing over the player's maximum health
            if self.__current_health > self.__health_max:
                self.__current_health = self.__health_max
                print(f"\nYour health is now: {self.__current_health}/{self.__health_max}")

            else:
                print(f"\nYour health is now: {self.__current_health}/{self.__health_max}")

    def update_vision(self, source):

        # Should have a "while loop" to time the length of the potion, or some limitation
        if source == Items.vision_potion:
            self.__vision_active = True
        return self.__vision_active
