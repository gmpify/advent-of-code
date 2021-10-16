import pytest
from app import *


def test_contains_three_vowels_in_order():
    v = ValidatorPartOne('aei')
    assert v.contains_three_vowels() is True


def test_contains_three_vowels_not_in_order():
    v = ValidatorPartOne('xazegov')
    assert v.contains_three_vowels() is True


def test_not_contains_three_vowels():
    v = ValidatorPartOne('dvszwmarrgswjxmb')
    assert v.contains_three_vowels() is False


def test_contains_repeated_letter():
    v = ValidatorPartOne('abcdde')
    assert v.contains_repeated_letter() is True


def test_not_contains_repeated_letter():
    v = ValidatorPartOne('jchzalrnumimnmhp')
    assert v.contains_repeated_letter() is False


def test_contains_only_allowed_substring():
    v = ValidatorPartOne('aaa')
    assert v.contains_only_allowed_substring() is True


def test_not_contains_only_allowed_substring():
    v = ValidatorPartOne('haegwjzuvuyypxyu')
    assert v.contains_only_allowed_substring() is False


def test_contains_repeated_substring():
    v = ValidatorPartTwo('xyxy')
    assert v.contains_repeated_substring() is True


def test_not_contains_repeated_substring():
    v = ValidatorPartTwo('aaa')
    assert v.contains_repeated_substring() is False


def test_contains_repeated_letter_distance_2():
    v = ValidatorPartTwo('xyx')
    assert v.contains_repeated_letter(2) is True


def test_contains_repeated_letter_distance_2():
    v = ValidatorPartTwo('abcdefeghi')
    assert v.contains_repeated_letter(2) is True


def test_contains_repeated_letter_distance_2():
    v = ValidatorPartTwo('aaa')
    assert v.contains_repeated_letter(2) is True
