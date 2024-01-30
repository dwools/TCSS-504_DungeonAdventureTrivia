# import HealingPotion
# """Creates the room class with constructors self, healing, vision, pit"""
# class Room:
#     """init function includes all features a room could have"""
#     def __init__(self, content = []):
#         self.content = []
#         self._northdoor = "N" in content
#         self._eastdoor = 'E' in content
#         self._westdoor = 'W' in content
#         self._southdoor = 'S' in content
#         self._entrance = 'i' in content
#         self._exit = 'O' in content
#         self._blocked = 'B' in content
#         self._entered = 'E' in content
#         self._empty_room = ' ' in content
#         self._multiple_items = 'M' in content
#         self._pit = 'X' in content
#         self._healing = 'H' in content
#         self._vision = 'V' in content
#         self._pillars = "A, E, I, P"
#         self._healing_points = random.randint(5, 15) if self._healing else 0
#
# # Make the northdoor, southdoor, etc their own paramters. Then the state of the doors is indepentent from
# #Then add the contents to a list.
#
# #my_room = Room()
# # my_room._northdoor = True
# # my_room._healing = True
# # my_room._pit = True
#
#     def __str__(self):
#         """
#         String function to create 2D visual of the rooms
#         """
#         room_design = ""
#         if self._northdoor:
#             room_design += "*_*"
#         else:
#             room_design += "***"
#         room_design += ("\n")
#         if self._westdoor:
#             room_design += "|"
#         else:
#             room_design += "*"
#         if self._pit:
#             room_design += "X"
#         elif self._entrance:
#             room_design += "i"
#         elif self._exit:
#             room_design += "O"
#         elif self._vision:
#             room_design += "V"
#         elif self._healing:
#             room_design += "H"
#         elif self._multiple_items:
#             room_design += "M"
#         elif self._pillars:
#             room_design += "A, E, I, P"
#         else:
#             room_design += " "
#         if self._eastdoor:
#             room_design += "|"
#         else:
#             room_design += "*"
#         room_design += ("\n")
#         if self._southdoor:
#             room_design += "*_*"
#         else:
#             room_design += "***"
#
#         return room_design
#
#     def __repr__(self):
#         return self.__str__()
#
#     # def __str__(self):
#     #     item_count = 0;
#     #     if self._healing:
#     #         item_count += 1
#     #     if self._vision:
#     #         item_count += 1
#     #
#     #     if item_count > 1:
#     #         return "M"
#     #     return "Health potion: " + str(self._healing) + "\n" \
#     #         + "Vision potion: " + str(self._vision) + "\n" \
#     #         + "Pillar: " + str(self._pillars) + "\n" \
#     #         + "Pit: " + str(self._pit) + "\n" \
#     #         + "Blocked: " + str(self._blocked) + "\n" \
#     #         + "Entrance: " + str(self._entrance) + "\n" \
#     #         + "Exit: " + str(self._exit) + "\n\n"
#
#
#     def set_healing(self, add_potion):
#         """Sets healing to be adding a potion"""
#         self._healing = add_potion
#
#     def get_healing_points(self):
#         return self._healing_points
#
#
#     def set_vision(self, add_vision_potion):
#         """Sets vision to be adding a vision potion"""
#         self._vision = add_vision_potion
#
#     def set_entered(self, entered):
#         """Sets if the room was entered already"""
#         self._entered = entered
#
#     def set_pillars(self, pillars):
#         """Sets the pillars of OO"""
#         self._pillars = pillars
#
#     @property
#     def can_enter(self):
#         """Sets if can enter a room"""
#         return not self._blocked and not self._entered
#
#     @property
#     def is_exit(self):
#         """Sets if is an exit"""
#         return self._exit
#
#     @property
#     def is_entrance(self):
#         """Sets if an entrance"""
#         return self._entrance
#
#     @property
#     def is_blocked(self):
#         """Sets if blocked"""
#         return self._blocked
#
#     @property
#     def is_not_blocked(self):
#         """Sets if not blocked"""
#         return not self._blocked
#
#     @property
#     def is_empty(self):
#         """Sets if empty"""
#         return not self._empty_room
#
#
#     # def get_health_chance(self):
#     #     return self._healthChance
#     #
#     # def get_vision_chance(self):
#     #     return self._visionChance
#     #
#     # def get_pillars_chance(self):
#     #     return self._pillarsChance
#
#
# # DUNGEON ADVENTURE PUBLIC METHODS
#     """public method to check for a door on the north end of the room"""
#     def has_north_door(self):
#         return self._northdoor
#
#     """public method to check for a door on the east end of the room"""
#     def has_east_door(self):
#         return self._eastdoor
#
#     """public method to check for a door on the west end of the room"""
#     def has_west_door(self):
#         return self._westdoor
#
#     """public method to check for a door on the south end of the room"""
#     def has_south_door(self):
#         return self._southdoor
#
#     """public method to check if a room has a healing potion in it"""
#     def has_healing_potion(self):
#         return self._healing
#
#     """public method to check if a room has a vision potion in it"""
#     def has_vision_potion(self):
#         return self._vision
#
#
#
# import random
# """Create RoomFactory class"""
# class RoomFactory:
#     @classmethod
#     def create_room(cls, row,col):
#         features = "" #intialize features
#         """Randomly choose which feature the room will contain"""
#         if random.randint(0, 100) <= 10:  # 10% chance for healing
#             features += 'H'
#         if random.randint(0, 100) <= 10:  # 10% chance for vision
#             features += 'V'
#         if random.randint(0, 100) <= 10:  # 10% chance for pit
#             features += 'X'
#         if random.randint(0, 100) <= 10:  # 10% chance for Pillars
#             features += 'A'
#             features += 'E'
#             features += 'I'
#             features += 'P'
#
#             # Only one room will have an entrance and the room that contains the entrance will contain NOTHING else
#         if row == 0 and col == 0:
#             features = 'i'
#             #Only one room will have an exit and the room that contains the exit will contain NOTHING else
#         if row == 2 and col == 2:
#             features = 'O'
#         # if random.randint(0, 100) <= 25:  # 10 % chance for door
#         #     features += 'N'
#         # if random.randint(0, 100) <= 25:  # 10 % chance for door
#         #     features += 'E'
#         # if random.randint(0, 100) <= 25:  # 10 % chance for door
#         #     features += 'W'
#         # if random.randint(0, 100) <= 25:  # 10 % chance for door
#         #     features += 'S'
#         return Room(features)
#
# room = RoomFactory.create_room(1, 0)
# print(room)
# # print(room.get_healing_points())
#     #def create_room(cls, has_healing = False, has_vision = False, has_pit = False):
#         #return Room("NEWSBE MiXOHVP")
#         #return Room(has_healing, has_vision, has_pit)
#         #healing_potions = random.randint(5, 15)
#         #pit = -random.randint(1, 20)
#
# #"""Sets up the random rolls for healing, vision, and pit"""
# #has_healing = random.randint(0, 100) <= 10
# #has_vision = random.randint(0, 100) <= 10
# #has_pit = random.randint(0, 100) <= 10
#
# """Use RoomFactory to create a room with random items"""
# #room_1 = RoomFactory.create_room(has_healing, has_vision, has_pit)
# #room_1._northdoor = True
# #room_1._eastdoor = True
# #room_1._westdoor = True
# #room_1._southdoor = True
# #room_1._vision = True
#
# #print(room_1)
