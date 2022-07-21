from app import *

def test_find_combinations():
    containers = [20, 15, 10, 5, 5]
    liters = 25
    assert len(find_combinations(liters, containers)) == 4

    expected_combinations = [
        (15, 10),
        (20, 5),
        (20, 5),
        (15, 5, 5),
    ]

    for combination in find_combinations(liters, containers):
        assert combination in expected_combinations
        expected_combinations.remove(combination)
