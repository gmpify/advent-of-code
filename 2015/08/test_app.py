import pytest
from app import *


@pytest.fixture
def test_file():
    f = open('test.txt', 'rb')
    return f.read().split()


@pytest.fixture
def line0(test_file):
    return test_file[0]


def test_line0(line0):
    assert get_literal_length(line0) == 2
    assert get_string_length(line0) == 0
    assert get_encoded_length(line0) == 6


@pytest.fixture
def line1(test_file):
    return test_file[1]


def test_line1(line1):
    assert get_literal_length(line1) == 5
    assert get_string_length(line1) == 3
    assert get_encoded_length(line1) == 9


@pytest.fixture
def line2(test_file):
    return test_file[2]


def test_line2(line2):
    assert get_literal_length(line2) == 10
    assert get_string_length(line2) == 7
    assert get_encoded_length(line2) == 16


@pytest.fixture
def line3(test_file):
    return test_file[3]


def test_line3(line3):
    assert get_literal_length(line3) == 6
    assert get_string_length(line3) == 1
    assert get_encoded_length(line3) == 11


def test_process_file():
    total_string_literals, total_string, total_string_encoded = process_file('test.txt')
    assert total_string_literals == 23
    assert total_string == 11
    assert total_string_encoded == 42
