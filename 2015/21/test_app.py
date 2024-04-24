from app import *
import pytest

def test_fight():
    boss = Character('boss', 12, 7, 2)
    player = Character('player', 8, 5, 5)

    fight = Fight(boss, player)
    fight.start()

    assert fight.winner is player

def test_equip():
    player = Character('player', 8, 5, 5)
    weapon = Weapon('dagger', 8, 4, 0)

    player.equip(weapon)

    assert player.damage == 9
    assert player.armor == 5

    armor = Armor('leather', 13, 0, 1)
    player.equip(armor)

    assert player.damage == 9
    assert player.armor == 6

def test_equip_more_than_one_weapon_fails():
    player = Character('player', 8, 5, 5)
    weapon = Weapon('dagger', 8, 4, 0)

    player.equip(weapon)
    with pytest.raises(Exception):
        player.equip(weapon)
