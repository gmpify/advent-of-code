import itertools

class Equipment:
    def __init__(self, name, cost, damage, armor) -> None:
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

class Weapon(Equipment):
    def __init__(self, name, cost, damage, armor) -> None:
        super().__init__(name, cost, damage, armor)

class Armor(Equipment):
    def __init__(self, name, cost, damage, armor) -> None:
        super().__init__(name, cost, damage, armor)

class Ring(Equipment):
    def __init__(self, name, cost, damage, armor) -> None:
        super().__init__(name, cost, damage, armor)

class Shop:
    def __init__(self) -> None:
        self.weapons = [
            Weapon("Dagger",      8, 4, 0),
            Weapon("Shortsword", 10, 5, 0),
            Weapon("Warhammer",  25, 6, 0),
            Weapon("Longsword",  40, 7, 0),
            Weapon("Greataxe",   74, 8, 0),
        ]

        self.armors = [
            Armor("Leather",    13, 0, 1),
            Armor("Chainmail",  31, 0, 2),
            Armor("Splintmail", 53, 0, 3),
            Armor("Bandedmail", 75, 0, 4),
            Armor("Platemail", 102, 0, 5),
        ]

        self.rings = [
            Ring("Damage +1",  25, 1, 0),
            Ring("Damage +2",  50, 2, 0),
            Ring("Damage +3", 100, 3, 0),
            Ring("Defense +1", 20, 0, 1),
            Ring("Defense +2", 40, 0, 2),
            Ring("Defense +3", 80, 0, 3),
        ]

    def combinations(self, min_weapon_count, max_weapon_count, min_armor_count, max_armor_count, min_ring_count, max_ring_count):
        weapons = []
        for weapon_count in range(min_weapon_count, max_weapon_count + 1):
            for w in itertools.combinations(self.weapons, weapon_count):
                weapons.append(w)
        
        armors = []
        for armor_count in range(min_armor_count, max_armor_count + 1):
            for a in itertools.combinations(self.armors, armor_count):
                armors.append(a)
        
        rings = []
        for ring_count in range(min_ring_count, max_ring_count + 1):
            for r in itertools.combinations(self.rings, ring_count):
                rings.append(r)

        equipments = []
        for weapon_group in weapons:
            for armor_group in armors:
                for ring_group in rings:
                    equipment = []
                    equipment.extend(weapon_group)
                    equipment.extend(armor_group)
                    equipment.extend(ring_group)

                    equipments.append(equipment)

        return equipments

class Character:
    def __init__(self, name, hit_points, damage, armor) -> None:
        self.name = name
        self.hit_points = hit_points
        self._damage = damage
        self._armor = armor
        self.damage = self._damage
        self.armor = self._armor

        self.weapon_equiped = None
        self.armor_equiped = None
        self.rings_equiped = set()
    
    def equip(self, equipment):
        if isinstance(equipment, Weapon):
            if self.weapon_equiped is not None:
                raise Exception("Already have weapon")
            self.weapon_equiped = equipment
        elif isinstance(equipment, Armor):
            if self.armor_equiped is not None:
                raise Exception("Already have armor")
            self.armor_equiped = equipment
        elif isinstance(equipment, Ring):
            if len(self.rings_equiped) >= 2:
                raise Exception("Already have 2 rings")
            self.rings_equiped.add(equipment)
        else:
            raise Exception(f"Can't equip that {equipment}")
        
        self.damage += equipment.damage
        self.armor += equipment.armor

class Fight:
    def __init__(self, boss, player):
        self.defender = boss
        self.attacker = player
        self.winner = None

    def start(self):
        while not self.winner:
            self.do_turn()

    def do_turn(self):
        turn_damage = self.attacker.damage - self.defender.armor
        if turn_damage < 1:
            turn_damage = 1
        
        self.defender.hit_points -= turn_damage
        if self.defender.hit_points <= 0:
            self.winner = self.attacker

        self.attacker, self.defender = self.defender, self.attacker

def combination_cost(equipment):
    result = 0
    for e in equipment:
        result += e.cost
    return result

if __name__ == '__main__':
    shop = Shop()
    equipment_combinations = shop.combinations(
        min_weapon_count=1,
        max_weapon_count=1,
        min_armor_count=0,
        max_armor_count=1,
        min_ring_count=0,
        max_ring_count=2
    )
    exit
    equipment_combinations.sort(key=combination_cost)

    for equipment in equipment_combinations:
        boss = Character('boss', 104, 8, 1)

        player = Character('player', 100, 0, 0)
        for e in equipment:
            player.equip(e)

        print(player.damage)
        print(player.armor)
        fight = Fight(boss, player)
        fight.start()

        print("=====")
        print(f"Equipment cost: {combination_cost(equipment)}.")
        print(f"Winner is: {fight.winner.name}.")

        if fight.winner == player:
            break
