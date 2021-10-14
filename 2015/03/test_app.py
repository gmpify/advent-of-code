import pytest
from app import Santa


def test_move_north():
    s = Santa()
    s.move('^')

    assert s.position() == (0, 1)
    assert s.houses_visited() == 2


def test_move_south():
    s = Santa()
    s.move('v')

    assert s.position() == (0, -1)
    assert s.houses_visited() == 2


def test_move_east():
    s = Santa()
    s.move('>')

    assert s.position() == (1, 0)
    assert s.houses_visited() == 2


def test_move_west():
    s = Santa()
    s.move('<')

    assert s.position() == (-1, 0)
    assert s.houses_visited() == 2


def test_square_instructions():
    s = Santa()
    s.move('^>v<')

    assert s.houses_visited() == 4


def test_line_instructions():
    s = Santa()
    s.move('^v^v^v^v^v')

    assert s.houses_visited() == 2
