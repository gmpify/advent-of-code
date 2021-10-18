import pytest
from app import *


@pytest.fixture
def light():
    return StandardLight()


@pytest.fixture
def dimmable_light():
    return DimmableLight()


def test_light_turn_on_and_off(light):
    assert light.brightness == StandardLight.OFF
    light.turn_on()
    assert light.brightness == StandardLight.ON
    light.turn_off()
    assert light.brightness == StandardLight.OFF


def test_light_toggle(light):
    assert light.brightness == StandardLight.OFF
    light.toggle()
    assert light.brightness == StandardLight.ON
    light.toggle()
    assert light.brightness == StandardLight.OFF


def test_dimmable_light_turn_on_and_off(dimmable_light):
    assert dimmable_light.brightness == 0
    dimmable_light.turn_off()
    assert dimmable_light.brightness == 0
    dimmable_light.turn_on()
    assert dimmable_light.brightness == 1
    dimmable_light.turn_off()
    assert dimmable_light.brightness == 0


def test_dimmable_light_toggle(dimmable_light):
    assert dimmable_light.brightness == 0
    dimmable_light.toggle()
    assert dimmable_light.brightness == 2
    dimmable_light.toggle()
    assert dimmable_light.brightness == 4


def test_light_command(light):
    assert light.brightness == StandardLight.OFF
    light.command('turn on')
    assert light.brightness == StandardLight.ON
    light.command('turn off')
    assert light.brightness == StandardLight.OFF
    light.command('toggle')
    assert light.brightness == StandardLight.ON


def test_point():
    p = Point(1, 2)
    assert p.x == 1
    assert p.y == 2


def test_point_parse():
    point = Point.parse('0,1')
    assert point == Point(0, 1)


def test_grid_count():
    grid = Grid()
    assert grid.count_lights() == 0


def test_grid_parse_command():
    grid = Grid()
    assert grid.parse_command('turn on 0,0 through 999,999') == ('turn on', Point(0,0), Point(999,999))
    assert grid.parse_command('toggle 0,0 through 999,0') == ('toggle', Point(0, 0), Point(999, 0))
    assert grid.parse_command('turn off 499,499 through 500,500') == ('turn off', Point(499, 499), Point(500, 500))


def test_grid_run_command():
    grid = Grid()
    assert grid.count_lights() == 0
    grid.run_command('turn on 0,0 through 999,999')
    assert grid.count_lights() == 1_000_000

def test_grid__dimmable_lights_run_command():
    grid = Grid(light=DimmableLight)
    assert grid.count_lights() == 0
    grid.run_command('toggle 0,0 through 999,999')
    assert grid.count_lights() == 2_000_000
