from app import *

def initial_state():
    return open('test_input.txt').read().strip()

def test_lights_on_count():
    grid = Grid(initial_state())
    assert grid.count_lights_on() == 15

def test_steps():
    grid = Grid(initial_state())
    grid.step()
    assert grid.count_lights_on() == 11
    grid.step()
    assert grid.count_lights_on() == 8
    grid.step()
    assert grid.count_lights_on() == 4
    grid.step()
    assert grid.count_lights_on() == 4
