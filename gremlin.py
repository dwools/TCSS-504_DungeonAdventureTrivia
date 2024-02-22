import monster


class Gremlin(Monster):
    def __init__(self, name,
                 hit_points,
                 attack_speed,
                 chance_to_hit,
                 minimum_damage,
                 maximum_damage,
                 chance_to_heal,
                 minimum_heal_points,
                 maximum_heal_points):
        super().__init__(name,
                         hit_points,
                         attack_speed,
                         chance_to_hit,
                         minimum_damage,
                         maximum_damage,
                         chance_to_heal,
                         minimum_heal_points,
                         maximum_heal_points)
