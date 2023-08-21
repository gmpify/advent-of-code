from app import *

def test_first_house():
    street = Street(1)
    street.visit_houses()
    assert street.houses[0].presents == 10

def test_fourth_house():
    street = Street(4)
    street.visit_houses()
    assert street.houses[3].presents == 70
