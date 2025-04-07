from character import Character

class Monster(Character):
    def __init__(self):
        super().__init__()

    def monster_attacks(self, hero):
        damage = self.combat_strength
        print(f"Monster attacks the hero for {damage} damage!")
        hero.health_points -= damage if hero.health_points - damage >= 0 else 0
        print(f"Hero now has {hero.health_points} health remaining.")

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector")
        super().__del__()
