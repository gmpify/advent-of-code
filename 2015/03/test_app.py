import pytest
from app import *

def test_simple_instructions():
    d = DistributionPlan('>')
    d.execute()

    assert d.houses_visited() == 2


def test_square_instructions():
    d = DistributionPlan('^>v<')
    d.execute()

    assert d.houses_visited() == 4


def test_line_instructions():
    d = DistributionPlan('^v^v^v^v^v')
    d.execute()

    assert d.houses_visited() == 2


def test_two_santas_simple_instructions():
    d = DistributionPlan('^v', 2)
    d.execute()

    assert d.houses_visited() == 3


def test_two_santas_square_instructions():
    d = DistributionPlan('^>v<', 2)
    d.execute()

    assert d.houses_visited() == 3


def test_two_santas_line_instructions():
    d = DistributionPlan('^v^v^v^v^v', 2)
    d.execute()

    assert d.houses_visited() == 11
