from character import Character

class Hero(Character):
    def __init__(self):
        super().__init__()

    def hero_attacks(self, monster):
        damage = self.combat_strength
        print(f"Hero attacks the monster for {damage} damage!")
        monster.health_points -= damage if monster.health_points - damage >= 0 else 0
        print(f"Monster now has {monster.health_points} health remaining.")

    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector")
        super().__del__()