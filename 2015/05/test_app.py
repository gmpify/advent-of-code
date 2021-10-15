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


def test_contains_repeated_letter():
    v = Validator('abcdde')
    assert v.contains_repeated_letter() is True


def test_not_contains_repeated_letter():
    v = Validator('jchzalrnumimnmhp')
    assert v.contains_repeated_letter() is False


def test_contains_only_allowed_substring():
    v = Validator('aaa')
    assert v.contains_only_allowed_substring() is True


def test_not_contains_only_allowed_substring():
    v = Validator('haegwjzuvuyypxyu')
    assert v.contains_only_allowed_substring() is False

