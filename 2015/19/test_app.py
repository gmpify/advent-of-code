from app import *

def test_hoh_replacements():
    replacement_rules = [
        "H => HO",
        "H => OH",
        "O => HH",
    ]
    starting_point = "HOH"
    machine = Machine(replacement_rules, starting_point)

    assert machine.distinct_molecules_count() == 4
