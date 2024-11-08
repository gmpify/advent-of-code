import copy

class Spell:
    def __init__(self, name, cost, turns_effective = 0, damage = 0, armor = 0, hit_points = 0, mana = 0) -> None:
        self.name = name
        self.cost = cost
        self.turns_effective = turns_effective

        self.damage = damage
        self.armor = armor
        self.hit_points = hit_points
        self.mana = mana
    
    def apply_effect(self, player):
        if self.damage > 0:
            player.damage += self.damage
        if self.armor > 0:
            player.armor += self.armor
        if self.hit_points > 0:
            player.hit_points += self.hit_points
        if self.mana > 0:
            player.mana += self.mana

class Boss:
    def __init__(self, hit_points, damage) -> None:
        self.hit_points = hit_points
        self.damage = damage
        self.armor = 0

class Player:
    def __init__(self, hit_points, mana) -> None:
        self.hit_points = hit_points
        self.mana = mana
        self.base_damage = 0
        self.base_armor = 0
        self.active_spells = {}
        self.total_mana_spent = 0

    def spells(self):
        return [
            Spell(name="Magic Missile", cost=53, damage=4),
            Spell(name="Drain", cost=73, damage=2, hit_points=2),
            Spell(name="Shield", cost=113, turns_effective=6, armor=7),
            Spell(name="Poison", cost=173, turns_effective=6, damage=3),
            Spell(name="Recharge", cost=229, turns_effective=5, mana=101)
        ]

    def is_spell_possible_for_turn(self, spell):
        return (spell.name not in self.active_spells and spell.cost <= self.mana)

    def apply_spell_effects(self):
        self.damage = self.base_damage
        self.armor = self.base_armor

        for _, spell in self.active_spells.items():
            spell.apply_effect(self)
            spell.turns_effective -= 1

        self.active_spells = {k: v for k, v in self.active_spells.items() if v.turns_effective > 0}

    def activate_spell(self, spell):
        self.total_mana_spent += spell.cost
        self.mana -= spell.cost
        self.damage = self.base_damage
        self.armor = self.base_armor

        if spell.turns_effective == 0:
            spell.apply_effect(self)
        else:
            self.active_spells[spell.name] = spell

class Fight:
    def __init__(self, boss, player, mode):
        self.boss = boss
        self.player = player
        
        self.attacker = "player"
        self.winner = None
        self.spells = []
        self.mode = mode

    def do_turn(self, spell):
        if spell is not None:
            self.spells.append(spell.name)

        if self.mode == "hard" and self.attacker == "player":
            self.player.hit_points -= 1
            if self.player.hit_points <= 0:
                self.winner = "boss"
                return

        self.player.apply_spell_effects()

        player_damage = self.player.damage - self.boss.armor
        self.boss.hit_points -= player_damage
        if self.boss.hit_points <= 0:
            self.winner = "player"
            return

        if self.attacker == "player":
            if not self.player.is_spell_possible_for_turn(spell):
                self.winner = "boss"
                return
            self.player.activate_spell(spell)
            player_damage = self.player.damage - self.boss.armor
            self.boss.hit_points -= player_damage
            if self.boss.hit_points <= 0:
                self.winner = "player"
                return
            self.attacker = "boss"
        elif self.attacker == "boss":
            boss_damage = self.boss.damage - self.player.armor
            if boss_damage < 1:
                boss_damage = 1
            self.player.hit_points -= boss_damage
            if self.player.hit_points <= 0:
                self.winner = "boss"
                return
            self.attacker = "player"

def find_fight_with_least_mana_used(boss, player, mode):
    fight_with_least_mana_used = None
    in_progress_fights = [Fight(boss, player, mode)]
    while len(in_progress_fights) > 0:
        fight = in_progress_fights.pop(0)

        if fight_with_least_mana_used is not None and fight.player.total_mana_spent > fight_with_least_mana_used.player.total_mana_spent:
            continue

        if fight.attacker == "boss":
            new_fight = copy.deepcopy(fight)
            new_fight.do_turn(None)
            if new_fight.winner == "player":
                if fight_with_least_mana_used is None or fight_with_least_mana_used.player.total_mana_spent > new_fight.player.total_mana_spent:
                    fight_with_least_mana_used = new_fight
            elif new_fight.winner is None:
                in_progress_fights.append(new_fight)
        else:
            for spell in player.spells():
                new_fight = copy.deepcopy(fight)
                new_fight.do_turn(spell)
                if new_fight.winner == "player":
                    if fight_with_least_mana_used is None or fight_with_least_mana_used.player.total_mana_spent > new_fight.player.total_mana_spent:
                        fight_with_least_mana_used = new_fight
                elif new_fight.winner is None:
                    in_progress_fights.append(new_fight)
    return fight_with_least_mana_used

if __name__ == "__main__":
    player = Player(50, 500)
    boss = Boss(51, 9)

    fight = find_fight_with_least_mana_used(boss, player, mode = "normal")
    print(f"Part 1 - Minimum mana needed to win fight: {fight.player.total_mana_spent}")

    fight = find_fight_with_least_mana_used(boss, player, mode = "hard")
    print(f"Part 2 - Minimum mana needed to win fight: {fight.player.total_mana_spent}")
