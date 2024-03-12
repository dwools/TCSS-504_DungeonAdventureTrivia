import random
from Room import Room

"""Create RoomFactory class"""
class RoomFactory:
    @classmethod
    def create_room(cls, features, doors, row, col):
        return Room(features, doors, row, col)
