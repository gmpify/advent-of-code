import pytest
from app import *


def test_contains_three_vowels_in_order():
    v = Validator('aei')
    assert v.contains_three_vowels() is True


def test_contains_three_vowels_not_in_order():
    v = Validator('xazegov')
    assert v.contains_three_vowels() is True


def test_not_contains_three_vowels():
    v = Validator('dvszwmarrgswjxmb')
    assert v.contains_three_vowels() is False

