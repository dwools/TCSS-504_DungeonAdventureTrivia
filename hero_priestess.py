from hero import Hero

class Priestess(Hero):
    def __init__(self, name, type, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage, chance_to_block, chance_to_heal, minimum_heal_points, maximum_heal_points):
        super().__init__(name, type, hit_points, attack_speed, chance_to_hit, minimum_damage, maximum_damage, chance_to_block)
        self.__chance_to_heal = chance_to_heal
        self.__minimum_heal_points = minimum_heal_points
        self.__maximum_heal_points = maximum_heal_points
