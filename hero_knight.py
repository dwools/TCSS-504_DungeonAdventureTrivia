from hero import Hero
class Knight(Hero):
    # to give a crushing blow is a CHOICE that the knight has.
    def __init__(self,
                 name,
                 type,
                 hit_points,
                 attack_speed,
                 chance_to_hit,
                 minimum_damage,
                 maximum_damage,
                 chance_to_block,
                 chance_for_crushing_blow,
                 minimum_crushing_damage,
                 maximum_crushing_damage):

        super().__init__(name,
                         type,
                         hit_points,
                         attack_speed,
                         chance_to_hit,
                         minimum_damage,
                         maximum_damage,
                         chance_to_block)

        self.__chance_for_crushing_blow = chance_for_crushing_blow
        self.__minimum_crushing_damage = minimum_crushing_damage
        self.__maximum_crushing_damage = maximum_crushing_damage

    def get_chance_for_crushing_blow(self):
        print(self.__chance_for_crushing_blow)
        return self.__chance_for_crushing_blow
